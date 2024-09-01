## Ohjelman yleisrakenne

Ohjelma on kivi-paperi-sakset-peli, jossa pelaajaa vastaan pelaa tekoäly, joka ennustaa pelaajan valintoja käyttämällä Trie-tietorakennetta. 
Ohjelma luokat tekevä seuraavia asioita:

RockPaperScissors (src/game.py)
- Pelin ydinluokka, joka hallitsee pelin kulkua. Pelin kulkuun kuuluvat mm. kierrosten määrän päivitys, AI mallien valinta ja tulosten näyttäminen.

ScoreManager (src/game_components.py)
- Huolehtii pisteiden laskemisesta ja säilyttämisestä pelin aikana. Näihin kuuluvat pelaajan ja AI:n pisteet sekä tasapelit.

LastSevenManager (src/game_components.py)
- Hallinnoi pelaajan viimeisten seitsemän siirron historiaa, jonka avulla Trie päivitetään ja mallit saavat syötteensä.

Node (src/trie.py)
- Kuvastaa Trie-tietorakenteen solmua. Jokaisella solmulla voi olla kolme lasta (yksi jokaiselle merkille: kivi, paperi, sakset) ja laskuri (frekvenssit), joka tallentaa kuinka monta kertaa tietty merkkijono on tullut vastaan.

Trie (src/trie.py)
- Trie-tietorakenne, joka tallentaa pelaajan aiemmat valinnat. Trie-rakennetta käytetään löytämään seuraavan merkin esiintymistodennäköisyydet, jotka perustuvat pelaajan aiempiin valintoihin. 

BaseAi (src/ai.py)
- Pohja luoda AI-malleja, jotka käyttävät Trie-rakennetta ennustamaan seuraavan pelaajan valinnan ja valitsevat ennustuksen voittavan merkin (k, p tai s). Käytän siis Markovin ketjuja. Niissä perusperiaate on, että tuleva tila riippuu vain nykyisestä tilasta, eikä aikaisemmista tiloista. Siten nykyinen tila on mallista riippuen määräytynyt 1-6 viimeisimmän pelaajan syöttämää merkkin mukaan ja tuleva tila ennustetaan Trie-rakenteen avulla.

AiSelector (src/ai.py)
- Valitsee parhaan tekoälymallin kuudesta eri vaihtoehdosta, joista jokainen analysoi eri pituisia pelaajan valintahistorioita. Nämä ovat siis 1-6 viimeistä siirtoa. Seuraavalle kierrokselle valitaan se malli, joka on menestynyt parhaiten viimeisten kierroksien aikana. Tämä kierrosten määrä on anntettu focus_lenght muuttujassa ja se on tällä hetkellä ohjelmassa 15.

## Saavutetut aika- ja tilavaativuudet

Trien kaikki operaatiot tapahtuvat ajassa O(n). Näihin operaatioihin kuuluvat lisäys, frekvenssien haku ja koko sisällön hakeminen. Ajassa O(n), n on käsiteltävän sanan pituus. Lähteiden mukaan trien haku vie aikaa pahimmillaan O(n) ja se aikavaativuus toteutuu työssäni.

## Tilastoja peleistä

### Tuttu 1

#### Pelin 1 tulokset
Pelaaja voitti 20 kertaa

Pelikone voitti 15 kertaa

Tasapeli tapahtui 15 kertaa

AI:n voittoprosentti: 30.0 %

#### Pelin 2 tulokset

Pelaaja voitti 17 kertaa

Pelikone voitti 17 kertaa

Tasapeli tapahtui 16 kertaa

AI:n voittoprosentti: 34.0 %

### Tuttu 2

#### Pelin 1 tulokset
Pelaaja voitti 9 kertaa

Pelikone voitti 18 kertaa

Tasapeli tapahtui 23 kertaa

AI:n voittoprosentti: 36.0 %

#### Pelin 2 tulokset
Pelaaja voitti 15 kertaa

Pelikone voitti 21 kertaa

Tasapeli tapahtui 14 kertaa

AI:n voittoprosentti: 42.0 %

#### Pelin 3 tulokset
Pelaaja voitti 11 kertaa

Pelikone voitti 20 kertaa

Tasapeli tapahtui 19 kertaa

AI:n voittoprosentti: 40.0 %

[Pelejä tarkemmin](https://github.com/labyrine/kivi-paperi-sakset/blob/main/docs/peli-tilastoja.md)

## Työn mahdolliset puutteet ja parannusehdotukset

- Tällä hetkellä AI-mallien määrää ei voi muuttaa helposti vaan se on aina 6. Koodia voisi muokata niin, että mallien määrän voi vaihtaa helpimmin.
- On ehkä epäintuitiivista, että tulostetaan seuraavalle kierrokselle tiedot parhaan mallin valintaan liittyen yms. Nämä tiedot voisi siirtää tulemaan vasta sille tarkoitetun pelitapahtuman jälkeen.
- AI-mallien valinnat perustuvat vain yksinkertaiseen frekvenssianalyysiin. Työtä voisi laajentaa kenties antamalla eri kirjaimille (k,p,s) todennäköisyydet, kuinka usein niitä kuuluu pelata tietyissä tilanteissa.
- Työlle voisi luoda grafiikat, niin sitä voisi olla mukavampi käyttää.

## Laajojen kielimallien käyttö

Käytin ChatGPT:tä projektin alussa auttamaan minua miettimään, miten haluaisin jakaa toiminnallisuuksia eri kansioihin. Projektia tehdessä olen käyttänyt sitä välillä selittämään minulle error-viestejä. Käytin sitä avuksi debuggausta varten käyttämieni tulostus-komentojen luonnissa onnistuneesti sekä epäonnistuneesti. Eli yritin silloin nopeuttaa yksinkretaisten koodinpätkien kirjoittamista. Käytin sitä myös RockPaperScissors luokan refaktorointiin pienempiin luokkiin: LastSevenManager ja ScoreManager.

## Lähteet
- [Trie](https://en.wikipedia.org/wiki/Trie)
- [Markovin ketjujen käyttö kivi-paperi-sakset pelissä](https://arxiv.org/pdf/2003.06769)
