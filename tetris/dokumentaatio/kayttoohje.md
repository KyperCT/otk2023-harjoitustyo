# Käyttöohje

Ohjelman uusimman palautetun version saa lataamalla uusimman julkaisun (releases) lähdekoodin julkaisun *assets* -osioista. Ohjelman uusimman kehitysversion saa kloonaamalla repositorion *main* -haaran.

### Alustus ja käynnistys

Repositorion ladattuasi sovelluksen asennus tehdään `tetris/` -kansiossa komennolla 

`poetry install`

jonka jälkeen sovelluksen voi käynnistää ajamalla

`poetry run invoke start`

### Aloitus

Peli alkaa painamalla näppäintä

### Pelaaminen

WASD- tai nuolinäppäimillä voi ohjata palikan liikettä. vasen, oikea ja alas liikuttavat liikkuvaa palaa näihin suuntiin, ylös kääntää palaa 90 astetta kellonsuuntaan.

### Sulkeminen

Sovelluksen voi sulkea millä hetkellä hyvänsä "Esc" -painikkeella

