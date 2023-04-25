# Vaatimusmäärittely

## Ohjelman tarkoitus

Ohjelma on toteutus tunnetusta tietokonepelistä "Tetris". Ohjelman pääasiallinen tarkoitus on mahdollistaa pelin pelaaminen. Tavoitteena on myös, että
ohjelma pitää kirjaa tuloksista.

## Perusversion toiminnallisuus

 - Ohjelma toteuttaa Tetriksen perustoiminnallisuuden \- tehty
   - Ohjelma näyttää pelikentän \- tehty
   - Kentän yläpäähän ilmestyy eri muotoisia paloja, joita pelaaja voi manipuloida sääntöjen mukaisesti \- tehty
   - Palat laskeutuu alaspäin vakionopeutta \- tehty
   - Paloja voi pyörittää 90 asteen vaiheissa \- tehty
   - Alaspäin laskeutumista voi nopeuttaa näppäimellä \- tehty
   - Kun palat osuu kentän pohjalle tai jo pelattuun palaan, pala jää paikalleen ja annetaan uusi pala \- tehty
   - jos palat täyttää kentän jossain rivissä kokonaan, palat katoaa ja rivin yläpuolella olevat rivit siirtyy kadonneen rivin tilalle \- tehty
   - Jos useampi rivi täyttyy samaan aikaan, ne kaikki katoaa ja ylemmät rivit siirtyy alkamaan alimman kadonneen rivin kohdalta \- tehty
   - Rivin täyttämisestä saa pisteitä, jotka näytetään pelinäkymässä \- tehty
   - Useamman rivin täytöstä saa enemmän pisteitä \- tehty
   - Peli päättyy, kun kentän ylimmällä rivillä on pala siten, että uutta palaa ei voi sijoittaa kentälle  \- tehty
 - Pelin päätyttyä ohjelma tarjoaa mahdollisuuden kirjata talteen pelin aikana kertyneet pisteet nimimerkillä
 - Ohjelmalla voi katsoa listaa aiemmista tuloksista suuruusjärjestyksessä

## Jatkotoiminnallisuutta

 - Tietyt pisterajat ylittäessä peli nopeutuu (siirtyy seuraavalle tasolle)
 - Palat ovat eri värisiä
 - Jonkinlainen tapa säätää palojen värejä
   - Peli muistaa asetukset

Jos oikeasti loppuu työt kesken:
 - Kentän kokoa voi säädellä
 - Jotain lisäsääntöjä
   - Kenttään ilmestyy satunnaisesti uusia paloja
   - Erikoispaloja jotka käyttäytyy epätavanomaisesti
 - Pistelistan voi tuoda ohjelmasta ulos ja ohjelmaan voi tuoda sisään kaverilta saatu pistelista
