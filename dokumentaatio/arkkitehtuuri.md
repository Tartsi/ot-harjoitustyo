# Arkkitehtuurikuvaus laskinsovellukselle

Viikko 5 - tallenushetkellä (26.04.2022) luokkakaavio seuraavanlainen:

![Luokkakaavio - Laskinsovellus](https://user-images.githubusercontent.com/62020899/165351637-bdb9dcc4-a877-4d14-bf27-800e776787fd.JPG)

Services-hakemiston calculator-luokka huolehtii itse laskimen luomisesta. UI tarkoituksena hallinnoida käyttäjälle näkyvää näkymää, oletusarvoisesti laskin, mutta tarkoituksena myöhemmin mahdollistaa myös laskuhistorian tutkiminen.

## Viikko 5 - tallennushetkellä (26.04.2022) sekvenssikaavio seuraavanlainen:

![Laskinsovellus, sekvenssikaavio](https://user-images.githubusercontent.com/62020899/165349528-cbd2bb32-1ee9-4a19-81db-2fba4feafdbc.JPG)

Sovelluksen käynnistyessä kutsutaan services-hakemiston calculator-luokkaa, joka luo laskinsovelluksen ja palauttaa käyttäjälle graafisen näkymän. Tämän jälkeen käyttäjä voi mielivaltaisesti manipuloida laskinta käyttäen tätä käyttöliittymää.

