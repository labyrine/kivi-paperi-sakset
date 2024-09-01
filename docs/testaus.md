# Testausdokumentti

Testaamiseen on käytetty unittest-kehystä. 

## Tekoälyn ja trie rakenteen integraatiotestaus

Simuloidaan peliä viidentoista kieroksen ajalta, kun focus_length on 5. Jokaisella kierroksella katsotaan, että trie rakenne palauttaa oikein sisältönsä ja sen perusteella valitaan parhaiten suoriutunut malli. Lopuksi verrataan, että nämä parhaiten suoriutuneet mallit ovat palauttaneet oikein seuraavan valintansa, mitä pelata. Tässä pitää kannattaa huomata, että paras malli ja sen valinta valitaan kierroksen lopuksi valmiiksi seuraavalle kierrokselle. 

## Yksikkötestauksen kattavuus

![Screenshot from 2024-09-01 19-45-06](https://github.com/user-attachments/assets/b4574397-6df7-4bce-8c98-05263796edc4)

trie.py
- Testattu yksikkötestein luokan funktiot add sekä get_next_frequencies. Lisäksi tätä käytetään integraatiotestauksessa, jolloin funktio get_all_strings_with_frequencies palauttaa verrattavaksi oikean trien sisällön.

ai.py
- Testattu yksikkötestein luokat BaseAi sekä AiSelector.

- BaseAi testauksen skenaarioihin kuuluvat mallin seuraavan valinnan hakeminen kun syöte on tarpeeksi pitkä (test_prediction_kps) tai lyhyt (test_prediction_short) tai tyhjä (test_prediction_empty). Syötteen ollessa tarpeeksi pitkä palautetaan seuraava mallin valinta. Muissa tapauksissa palautetaan tyhjä merkkijono. Lisäksi test_counter_move käy läpi tilanteet, joissa pelaajan syötteen perusteella malli valitsee, mitä sitä vastaan peltata sekä virheellisen valinnan. Integraatiotestaus vaikuttaa myös haaraumakattavuuteen.

- AiSelector testauksen skenaarioihin kuuluvat last_seven merkkijon päivittäminen jokaiselle mallille. Sekä mallien pisteet sisältävän listan (pisteet koostuvat edelliseltä focus length määrltä kierroksia) päivittäminen, kun tulee sekä voittoja ja häviöitä. Siinä testataan myös parhaan mallin valinnan toimivuus ja parhaan mallin seuraavan valinnan hakeminen, kun ennuste löytyy ja kun ennustetta ei löydy. Integraatiotestaus vaikuttaa myös haaraumakattavuuteen.

- Tavoite testien haaraumakattavuuden suhteen oli 100%. Tästä puuttuvat testaukset luokan AiSelector funktioille create_model_stats sekä def print_model_stats. Niiden toiminta ei kuitenkaan vaikuta itse pelin kulkuun ja AI:n toimintaan, vaan kerää voitot, häviöt ja tasapelit pelaajalle katsottavaksi. 

game_components.py
- Testattu yksikkötestein luokat ScoreManager sekä LastSevenManager, joita RockPaperScissors luokka kutsuu.

- ScoreManager luokkaa testatessa testataan kaikki skenaariot, joissa AI voi voittaa tai joissa ihminen voi voittaa.

- LastSevenManager luokkaa testattaessa testataan, että merkkijono last_seven päivitetään oikein kun se on lyhyempi kuin 7 ja kun se on pidempi kuin 7. Siinä testataan myös, että last_seven merkkijono tallennetaan oikein trie rakenteeseen kun se on pidempi kuin yksi ja kun se on vain yksi (tällöin sitä ei tallenneta). 

Tähän kattavuuteen ei lukeudu kansion game.py luokka RockPaperScissors.

### Muu testaus:
Kansion game.py luokka RockPaperScissors eli pelin silmukka sekä ihmisen pelille syötteiden antaminen on testattu useaan otteeseen manuaalisesti.
Luokan AiSelector funktiot create_model_stats sekä def print_model_stats on myös testattu manuaalisesti projektin teon loppupäässä.

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
