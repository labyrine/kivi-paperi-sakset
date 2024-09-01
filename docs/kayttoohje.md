# Käyttöohje

Ohjelma on kivi-paperi-sakset tekoäly. Sitä vastaan pelataan antamalla sille syötteinä pieniä kirjamia k (kivi), p (paperi) tai s (sakset). 

## Ohjelman käynnistäminen

### Riippuvuudet asennetaan terminaalissa kivi-paperi-sakset kansion sisällä komennolla

```bash
poetry install
```

### Pelin käynnistäminen tapahtuu komennolla

```bash
poetry run invoke start
```

## Muut komentorivitoiminnot

### Testaaminen

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

Raportti tulee generoitumaan _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemien tarkistusten suorittaminen

```bash
poetry run invoke lint
```
