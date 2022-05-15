# Käyttöohje

## Käynnistys

Asenna vaadittavat riippuvuudet:

```bash
poetry install
```

Käynnistys:

```bash
poetry run invoke start
```

## Laskinnäkymä

Aukeava näkymä on seuraavanlainen:

![Laskinsovellus - Kuva - Käyttöohje](https://user-images.githubusercontent.com/62020899/168491059-46c4eecc-6e84-4bec-b744-6bf1868ae72e.JPG)

Tässä käyttäjä voi nyt vapaasti suorittaa haluamiansa laskuja kuten kuvassa näkyy. C - nappi tyhjentää laskimen kentät ja H - nappi näyttää historian.
Saatavilla olevat laskimen toiminnot ovat luvun neliöinti, luvun neliöjuuri, plus-, miinus-, kerto- ja jakolasku.

## Historianäkymä

H-nappia painettaessa aukeava näkymä on seuraavanlainen:

![Laskinhistoria - Kuva - Käyttöohje](https://user-images.githubusercontent.com/62020899/168491120-6e0ec62f-1cba-4905-a1a1-44bab298c367.JPG)

Tässä näkyy käyttäjän tekemät laskut. Historia on tyhjä aina uuden laskinnäkymän auetessa. Käyttäjä voi myös tyhjentää historian manuaalisesti, mutta tällöin joutuu avaamaan historianäkymän uudelleen, jotta tyhjentäminen näkyisi.
