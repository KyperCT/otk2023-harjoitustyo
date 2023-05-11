# Arkkitehtuurikuvaus (5.2.)

## Rakenne

Ohjelman rakenne jakautuu viiteen osaan: Käyttöliittymästä vastaavaan pakettiin `gui`, tietokannasta vastaavaan pakettiin `database`, pelin olioista (palat, ruudukko) vastaavaan pakettiin `models`, olioiden interaktioista ja muusta pelilogiikasta vastaavaan pakettiin `logic` ja juurikansiossa sijaitsevaan `main.py` -moduuliin, joka yhdistää näitä paketteja (erityisesti käyttöliittymän muihin). Rakennetta kuvaa pakkauskaavio:

![pakkauskaavio](./kuvat/Pakkauskaavio.png)

Jossa nuolet edustavat riippuvaisuuksia (`main.py` riippuvainen kaikista, sisällytetty havainnollistaakseen rakennetta). Testipakkaus sisällytetty kuvaan, mutta ei ole osa sovelluksen tavanomaista toimintaa.

## Käyttöliittymä

Sovellus sulkeutuu kaikissa olosuhteissa Escape -näppäimestä.

Sovelluksella on kaksi näkymää:
 - Aloitusnäkymä, joka näytetään, kun peliä ei ole aloitettu tai se on loppunut. Peliin pääsee painamalla mitä nappia tahansa paitsi Escape -nappia.
 - Pelinäkymä, joka näyttää pelin tilan, eli ruudukon, pisteet ja putoavan palan.
 - Pelin loppunäkymä, joka näyttää saadut pisteet ja tarjoaa mahdollisuuden kirjata nimi pistettaulukkoa varten.

Aloitusnäkymässä näytetään 10 eniten pisteitä saanutta kirjausta pistetaulukosta.

Pelinäkymässä käyttäjä voi liikuttaa palaa nuolinäppäimillä ja "WASD" -näppäimillä. Peli päivittää näkymän ja vastaanottaa painalluksia 10 kertaa sekunnissa.

Loppunäkymässä voi kirjoittaa tavanomaisesti nimen, ja "Enter" -näppäimestä sovellus siirtyy takaisin aloitusnäkymään kirjaten annetun nimen ja pisteet pistetaulukkoon.

Käyttöliittymä on eristetty logiikasta käytännössä kokonaan. Käyttöliittymän ainoa riippuvuus on ruudukon luokkaan `Grid`, josta se tarkistaa mitkä ruudut merkitä täytetyiksi ja muuten sille toimitetaan vain pisteet kokonaislukuna. Vain osia yhdistävä `main()` -funktio kutsuu `gui/` -pakkauksen funktioita.

## Sovelluslogiikka

![logiikkakaavio](./kuvat/Logiikkakaavio.png)

Ylläoleva kaavio kuvaa sovelluksen loogista tiedonkulkua. Nuolet mallista kuvaa konstuktiota, muuten kyse on argumenteista tai palautuksista. Ruudukkoja on yksi ja pelilogiikka kutsuu sen metodeja muokatakseen sitä. Pelilogiikka luo palikoita tarvittaessa ja liikefunktiot kutsuu palikan metodeja liikuttaakseen sitä. Pelilogiikka käyttää palikoita määrittääkseen miltä ruudukon kuuluisi näyttää. Logiikka myös päivittää `score`  -arvon ja päivittää rivejä. Jos metodikutsut olisi kuvattuna, logiikasta menisi kutsuja malleihin kaikista funktioista.

## Pysyväistallennus

Pysyväistallennus tehdään SQLite tietokantaan, jonne tallennetaan pistetaulukko. Kanta on huomattavan yksinkertainen, ja sisältää vain yhden taulukon, jossa on nimimerkki, pistetulos ja uniikki id. SQL -kantaa on käytetty, koska tietojen hakeminen on SQL -komennolla huomattavan helppoa.

Tallennus on eriytetty muusta koodista, eli sen voisi muuttaa suhteellisen helposti toisenlaiseen ratkaisuun.

## Pelin kulkua sekvenssikaavioilla

### Pelin käynnistys

HUOM: Kuvauksessa ei ole tietokannan kanssa interaktioita, sillä ne ei suoraan vaikuta aloitusprosessiin.

```mermaid
sequenceDiagram
    actor User
    participant gui/
    participant main()
    participant other*
    main() ->> gui/ : render menu
    gui/ -->> User : Menu view
    main() ->> gui/ : is key pressed?
    User ->> gui/ : keypress
    gui/ -->> main() : True
    main() ->> main() : normal game loop start
    main() ->> other* : [calls]
    other* -->> main() : [returns]
    main() ->> gui/ : render game
    gui/ -->> User : Game view
```


### Pelin validi kierros (jolla peli ei liikuta palaa)

```mermaid
sequenceDiagram
    actor User
    participant gui/
    participant main()
    participant logic/
    participant model/Grid
    participant model/Block
    gui/ -->> User : Game view
    main() ->> gui/ : is relevant key pressed?
    User ->> gui/ : left arrowkey
    gui/ -->> main() : left
    main() ->> logic/ : state, key(left)
    logic/ ->> logic/ : user_move(left)
    logic/ ->> model/Block : get points
    model/Block -->> logic/ : points
    logic/ ->> model/Grid : Clear block points
    logic/ ->> model/Block : move_left
    logic/ ->> model/Grid : is grid at new block full?
    model/Grid -->> logic/ : False
    logic/ ->> model/Block : get points
    model/Block -->> logic/ : points
    logic/ ->> model/Grid : Update grid
    logic/ -->> main() : state
    main() ->> gui/ : render game
    gui/ ->> model/Grid : Where is the grid filled?
    model/Grid -->> gui/ : (grid points)
    gui/ -->> User : Game view
```

Jos palikkaa ei voi siirtää, niin kierros on lähes identtinen, vain täyden ruudukon kohdalla palikalle olisi tehty kutsu "unmove()" ja muuten jatkettu samalla tavalla

### Pelin kierros, kun peli liikuttaa palaa ja rivi täyttyy (ja käyttäjä sattumalta ei)

```mermaid
sequenceDiagram
    actor User
    participant gui/
    participant main()
    participant logic/
    participant model/Grid
    participant model/Block
    gui/ -->> User : Game view
    main() ->> gui/ : is relevant key pressed?
    User ->> gui/ : left arrowkey
    gui/ -->> main() : left
    main() ->> logic/ : state, key(-)
    logic/ ->> logic/ : is game turn, game_move
    logic/ ->> model/Block : get points
    model/Block -->> logic/ : points
    logic/ ->> model/Grid : Clear block points
    logic/ ->> model/Block : move_down
    logic/ ->> model/Grid : is grid at new block full?
    model/Grid -->> logic/ : False
    logic/ ->> model/Block : get points
    model/Block -->> logic/ : points
    logic/ ->> model/Grid : Update grid
    logic/ ->> logic/ : check score
    logic/ ->> model/Grid : Is row full? (n times)
    model/Grid -->> logic/ : [some return is True]
    logic/ ->> model/Grid : Remove row, shift above
    logic/ ->> logic/ : update score
    logic/ -->> main() : state
    main() ->> gui/ : render game
    gui/ ->> model/Grid : Where is the grid filled?
    model/Grid -->> gui/ : (grid points)
    gui/ -->> User : Game view
```

### Muu

Peli päättyy jos uutta palikkaa ei voi luoda ilman konfliktia, jolloin logiikka kertoo juurelle että peli on ohi. Tämä muistuttanee aloitusta jokseenkin, sillä lisäyksellä, että tietokantaan tehdään kirjaus.

Muuten pelin vuorot menee aikalailla kuvatusti riippumatta mitä liikkeitä tehdään. pelaaja ja peli voi liikuttaa palaa samalla vuorolla ja se voi onnistua tai olla onnistumatta. Pelaajan liike aina katsotaan ensin.

## Sovelluksen toteutuksen heikkoudet rakenteen kannalta

Palikoiden malli itse estää palikoita menemästä rajojen yli. Tämä on ongelma, koska mallin on tarkoitus olla täysin tietämätön ruudukosta. Enemmällä ajalla se tulisi refaktoroida siten, että kaikki rajatarkistukset siirtyisi logiikan puolelle, jotta palikka malli mallintaisi vaan abstraktia palikkaa jossain koordinaatistossa.

## Tämän dokumentaation heikkoudet

Sekvenssikaaviot ovat rajallisia ollakseen luettavia. Järkevä kuvaus vaatisi muutaman lisää, ainakin uuden palikan luonti voisi vielä kaivata. Kuitenkin näitä on jo aika monta, joten jottei dokumentti paisu kaikkia ei kuvata mielekkäästi. Logiikka- ja pakkauskaaviot eivät ole kovin selkeitä nykymuodossaan ja en ole varma miten selkeiten kaaviolla kuvata ohjelman rakennetta (vaikka rakenne itsessään on huomattavan luonteva mielestäni).