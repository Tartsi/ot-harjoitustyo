# Arkkitehtuurikuvaus laskinsovellukselle

Viikko 4 - tallenushetkellä luokkakaavio seuraavanlainen:

![Luokkakaavio - Laskinsovellus](https://user-images.githubusercontent.com/62020899/163041856-3ea76e23-96dd-4a4b-aa23-eb6f60375afd.JPG)

User ei itsessään ole luokka vaan sen on tarkoitus kuvata käyttäjää. Laskinsovellukseni laajentuessa päivitän luokkakaaviota, mutta alustavasti tilanne on suurinpiirtein tämä.

## Viikko 5 - tallennushetkellä (26.04.2022) sekvenssikaavio seuraavanlainen:

![Laskinsovellus, sekvenssikaavio](https://user-images.githubusercontent.com/62020899/165349528-cbd2bb32-1ee9-4a19-81db-2fba4feafdbc.JPG)

Sovelluksen käynnistyessä kutsutaan services-hakemiston calculator-luokkaa, joka luo laskinsovelluksen ja palauttaa käyttäjälle graafisen näkymän. Tämän jälkeen käyttäjä voi mielivaltaisesti manipuloida laskinta käyttäen tätä käyttöliittymää.
