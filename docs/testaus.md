# Testausdokumentti

Testaamiseen on käytetty unittest-kehystä. 

## Tekoälyn ja trie rakenteen integraatiotestaus

## Yksikkötestauksen kattavuus

![Screenshot from 2024-09-01 19-45-06](https://github.com/user-attachments/assets/b4574397-6df7-4bce-8c98-05263796edc4)

trie.py
- Testattu yksikkötestein luokan funktiot add sekä get_next_frequencies. Lisäksi tätä käytetään integraatiotestauksessa, jolloin funktio get_all_strings_with_frequencies palauttaa verrattavaksi oikean trien sisällön.

ai.py
- Testattu yksikkötestein luokat BaseAi sekä AiSelector.

- BaseAi testauksen skenaarioihin kuuluvat mallin seuraavan valinnan hakeminen kun syöte on tarpeeksi pitkä (test_prediction_kps) tai lyhyt (test_prediction_short) tai tyhjä (test_prediction_empty). Syötteen ollessa tarpeeksi pitkä palautetaan seuraava mallin valinta. Muissa tapauksissa palautetaan tyhjä merkkijono. Lisäksi test_counter_move käy läpi tilanteet, joissa pelaajan syötteen perusteella malli valitsee, mitä sitä vastaan peltata sekä virheellisen valinnan.

Tavoite testien haaraumakattavuuden suhteen oli 100%. Tästä puuttuvat testaukset luokan AiSelector funktioille create_model_stats sekä def print_model_stats. Niiden toiminta ei kuitenkaan vaikuta itse pelin kulkuun ja AI:n toimintaan, vaan kerää voitot, häviöt ja tasapelit pelaajalle katsottavaksi. 

Tähän kattavuuteen ei lukeudu kansion game.py luokka RockPaperScissors.

### Muu testaus:
Kansion game.py luokka RockPaperScissors eli pelin silmukka sekä ihmisen pelille syötteiden antaminen on testattu useaan otteeseen manuaalisesti.

## Yksikkötestien suorittaminen

### Riippuvuudet asennetaan terminaalissa kivi-paperi-sakset kansion sisällä komennolla

```bash
poetry install
```

### Testit ajetaan komennolla

```bash
poetry run invoke test
```

### Testikattavuusraportin saa generoitua komennolla


### Testikattavuus

```bash
poetry run invoke coverage-report
```

Raportti tulee generoitumaan _htmlcov_-hakemistoon.
