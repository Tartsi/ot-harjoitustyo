# Arkkitehtuurikuvaus laskinsovellukselle

## Luokkakaavio kuvaus rakenteelle:

![Luokkakaavio - Laskinsovellus #3](https://user-images.githubusercontent.com/62020899/168492160-24f32036-95b2-461e-acc6-3c7738d04524.JPG)

UI-hakemistossa sijaitsevan calculator_view-tiedoston tarkoituksena on luoda laskinnäkymä. Tämä calculator_view-tiedosto sitten kutsuu tiettyjä metodeita services-hakemiston calculator_service-tiedostosta liittyen laskemiseen. Nämä metodit mahdollistavat laskimen toiminnan ja vastaavat laskimen sovelluslogiikasta. UI-hakemiston history_view-tiedosto taas vastaa laskimen historianäkymästä ja on yhteistoiminnassa Repositories-hakemiston kanssa, missä laskuhistorian laskuja käsittelevät toiminnallisuudet sijaitsevat.

## Viikko 5 - tallennushetkellä (26.04.2022) sekvenssikaavio seuraavanlainen:

![Sekvenssikaavio - Laskinsovellus](https://user-images.githubusercontent.com/62020899/168492998-f82e47d5-6eb0-458f-b29b-5e7361c8ccab.JPG)

Sovelluksen käynnistyessä kutsutaan calculator_view-luokan run metodia, joka käynnistää käyttäjälle graafisen näkymän. Tämän jälkeen käyttäjä voi mielivaltaisesti manipuloida laskinta käyttäen tätä käyttöliittymää. Laskinnäkymä hyödyntää tämän jälkeen calculator_servicen metodeita liittyen laskutoimituksiin. Tämä luokka myös vastaa laskuhistorian päivittämisestä ja näkymän avaamisesta. Historianäkymän luomisesta vastaa history_view luokka ja tämä lopulta näyttää laskuhistoriassa olevat laskut yhtälöineen ja vastauksineen.
