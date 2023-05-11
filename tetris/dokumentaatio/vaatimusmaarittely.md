# Vaatimusmäärittely

## Ohjelman tarkoitus

Ohjelma on toteutus tunnetusta tietokonepelistä "Tetris". Ohjelman pääasiallinen tarkoitus on mahdollistaa pelin pelaaminen. Tavoitteena on myös, että
ohjelma pitää kirjaa tuloksista.

## Toiminnallisuus

 - Ohjelma toteuttaa Tetriksen perustoiminnallisuuden
   - Ohjelma näyttää pelikentän
   - Kentän yläpäähän ilmestyy eri muotoisia paloja, joita pelaaja voi manipuloida sääntöjen mukaisesti
   - Palat laskeutuu alaspäin vakionopeutta
   - Paloja voi pyörittää 90 asteen vaiheissa
   - Alaspäin laskeutumista voi nopeuttaa näppäimellä
   - Kun palat osuu kentän pohjalle tai jo pelattuun palaan, pala jää paikalleen ja annetaan uusi pala
   - jos palat täyttää kentän jossain rivissä kokonaan, palat katoaa ja rivin yläpuolella olevat rivit siirtyy kadonneen rivin tilalle
   - Jos useampi rivi täyttyy samaan aikaan, ne kaikki katoaa ja ylemmät rivit siirtyy alkamaan alimman kadonneen rivin kohdalta
   - Rivin täyttämisestä saa pisteitä, jotka näytetään pelinäkymässä
   - Useamman rivin täytöstä saa enemmän pisteitä
   - Peli päättyy, kun kentän ylimmällä rivillä on pala siten, että uutta palaa ei voi sijoittaa kentälle
 - Pelin päätyttyä ohjelma tarjoaa mahdollisuuden kirjata talteen pelin aikana kertyneet pisteet nimimerkillä
 - Ohjelmalla voi katsoa listaa aiemmista tuloksista suuruusjärjestyksessä
