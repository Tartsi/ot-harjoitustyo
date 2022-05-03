# Arkkitehtuurikuvaus laskinsovellukselle

Viikko 6 - tallenushetkellä (03.05.2022) luokkakaavio seuraavanlainen:

![Luokkakaavio - Laskinsovellus](https://user-images.githubusercontent.com/62020899/166562026-baaac20a-5719-44d6-b2cb-c59e93e5b0dd.JPG)

UI-hakemistossa sijaitsevan calculator_view-tiedoston tarkoituksena on luoda laskinnäkymä. Tämä calculator_view-tiedosto sitten kutsuu metodeita services-hakemistosta ja calculator-tiedostosta. Nämä metodit mahdollistavat laskimen toiminnan ja vastaavat laskimen sovelluslogiikasta. calculator-luokka kutsuu edelleen repositorio-hakemiston history_repository-tiedostoa ja sen metodeita mahdollistaen laskimen historianäkymän toiminnan.

## Viikko 5 - tallennushetkellä (26.04.2022) sekvenssikaavio seuraavanlainen:

![Laskinsovellus, sekvenssikaavio](https://user-images.githubusercontent.com/62020899/165349528-cbd2bb32-1ee9-4a19-81db-2fba4feafdbc.JPG)

HUOM! Sekvenssikaavio jää päivittämättä viikkoon 6 ja release 2 mennessä!

Sovelluksen käynnistyessä kutsutaan services-hakemiston calculator-luokkaa, joka luo laskinsovelluksen ja palauttaa käyttäjälle graafisen näkymän. Tämän jälkeen käyttäjä voi mielivaltaisesti manipuloida laskinta käyttäen tätä käyttöliittymää.
