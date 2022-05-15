# Arkkitehtuurikuvaus laskinsovellukselle

## Luokkakaavio kuvaus rakenteelle:

![Luokkakaavio - Laskinsovellus #3](https://user-images.githubusercontent.com/62020899/168492160-24f32036-95b2-461e-acc6-3c7738d04524.JPG)

Kaavion ja selvityksen tarkoituksena kuvastaa lopullista sovelluksen toimintaa!

UI-hakemistossa sijaitsevan calculator_view-tiedoston tarkoituksena on luoda laskinnäkymä. Tämä calculator_view-tiedosto sitten kutsuu metodeita services-hakemistosta ja calculator-tiedostosta. Nämä metodit mahdollistavat laskimen toiminnan ja vastaavat laskimen sovelluslogiikasta. calculator-luokka kutsuu edelleen repositorio-hakemiston history_repository-tiedostoa ja sen metodeita mahdollistaen laskimen historianäkymän toiminnan.

## Viikko 5 - tallennushetkellä (26.04.2022) sekvenssikaavio seuraavanlainen:

![Laskinsovellus, sekvenssikaavio](https://user-images.githubusercontent.com/62020899/165349528-cbd2bb32-1ee9-4a19-81db-2fba4feafdbc.JPG)

HUOM! Sekvenssikaavio jää päivittämättä viikkoon 6 ja release 2 mennessä!

Sovelluksen käynnistyessä kutsutaan services-hakemiston calculator-luokkaa, joka luo laskinsovelluksen ja palauttaa käyttäjälle graafisen näkymän. Tämän jälkeen käyttäjä voi mielivaltaisesti manipuloida laskinta käyttäen tätä käyttöliittymää.

