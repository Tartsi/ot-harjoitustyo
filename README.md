# Laskinsovellus

## Ohjelmistotekniikka-kurssi

- Sovelluksen avulla käyttäjä pystyy suorittamaan laskutoimituksia graafisella laskimella.
- Käytetty Python versio 3.9.5

### Linkit Dokumentaatioihin:

- [Vaatimusmäärittely](https://github.com/Tartsi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) 
- [Työaikakirjanpito](https://github.com/Tartsi/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](https://github.com/Tartsi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/Tartsi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/Tartsi/ot-harjoitustyo/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

### Asennus ja käyttöönotto:

```bash
poetry install
```

2. Käynnistys:

```bash
poetry run invoke start
```

3. Testit:

```bash
poetry run invoke test
```

4. Kattavuusraportti:

```bash
poetry run invoke coverage-report
```
