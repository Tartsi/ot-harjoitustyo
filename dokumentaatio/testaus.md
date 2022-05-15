# Testausdokumentti

- Ohjelma testattu unittestiä hyödyntäen
- Käyttöliittymä (ui-hakemiston) tiedostoja ei testattu

## Kattavuusraportti

![Testikattavuusraportti](https://user-images.githubusercontent.com/62020899/168492515-7b8b13f4-219d-4db9-af47-981ce4ea30a7.JPG)

- Testit keskittyvät laskimen sovelluslogiikkan metodeihin ja laskuhistorian käsittelyyn käytettyihin metodeihin.

# Sovellukseen jääneet ongelmat

- En saanut käsiteltyä tilannetta missä yksittäinen yhtälö käsittelee kerralla todella isoja laskutoimituksia esim. 99**99**99, toisaalta kyseinen lasku ääritapaus itsessään. Suurin osa muista vastaavista tilanteista käsitelty
