# Viikkoraportti 6
Tällä viikolla kävin läpi uudestaan paperia markovin ketjusita. 
Lisäksi nostin pelin kierrosten määrää ja se on nyt 50 sekä lisäsin printtaukset, jotka kertovat onko AI valinnut mitä pelata datan perusteella vai joutunut ottamaan satunnaisen valinnan. 
Sain perheenjäsenen pelaamaan peliä tekoälyä vastaan 3 peliä, mutta laitan datan varmaan toteutusdokumenttiin, jos se olisi kiinnostavaa. 
Huomasin vertaisarviosta, että ongelma AI:n valinnassa ja statistiikoissa, mitä ihmettelin aiemmin johtui siitä, että olin tehnyt aluksi yhden kierroksen perusteella toimivan AI:n enkä viiden.
Tein sen siksi, että saisin AI:sta vain jonkinlaisen toimivan ensimmäisen version. 
Ja sitten unohdin, että olin jättänyt sen osan kesken enkä lukenut koodiani uudestaan tarkemmin, kun aloitin kurssin uudestaan. 
Joten korjasin sen nyt viimein. 

Sitten luin muistiinpanojani testaus luennolta. 
Tein trie-rakenteeseen uudet funktiot, jotka palauttavat merkkijonon ja sen frekvenssin triestä. 
Yritin tehdä ensimmäiset versiot koko pelin testauksesta. 
Eli ensin tarkistetaan, että trie palauttaa oman sisältönsä oikein, sen perusteella katsotaan, että valitaan paras AI. 
Sitten katsotaan, että AI tekee oikean valinnan / pelataan oikea valinta. 

Nyt projektini toimii siis siten, että jokaisella kierroksella tekoälyt peluutetaan edellisen viiden (folus_length pituus) kierroksen mukaisesti. 
Jos pelillä ei ole riittävästi dataa tehdä veikkausta tai malli ei löydä sopivaa veikkausta, niin pelin tulos randomisoidaan.

Minun kannattaa tehdä joillekin yksittäisille tärkeille funktioille yksikkötestejä vielä. 
Ja jatkaa integraatiotestausta, koska minulla on tällä hetkellä vain yksi tapaus, mitä testata.
Seuraavaksi minun pitää tehdä toteutus ja testaus dokumentit. 
Sekä katsoa, miten pääsen eroon pylint virheistä. 
Lisäksi nimeäminen osassa funktiossa oli vertaisarvioijan mukaan ei niin osuvaa, joten katson nekin läpi. 
En usko enää aikovani käyttää trien poistotoimintoa työssäni, joten poistan sen ja katson onko minulla muuta ylimääräistä koodia jossain. 
Lisäksi saatan refaktoroida koodia mahdollisuuksien mukaan.

#### Kysymykset
- Riittääkö, että mietin erilaisia skenaarioita, joita testata (toistuvat merkkijonot, täysin randomi merkkijono yms) vai olisiko minun pitänyt testata muutosten vaikutuksia jokaisella kierroksella?
(En muista tätä asiaa luennolta) 
Ja jos minun pitäisi tehdä niin, miten se kannattaa toteuttaa? 
Kannattaako minun tehdä apufunktio, joka simuloi minulle yhden pelin, jota sitten testata?
- Onko ok, jos AI:t peluutetaan jokaisella kierroksella ja ne eivät pitäydy muutamassa tietyssä mallissa pelin aikana?
Tästä oli jotain keskustelua, että niiden kannattaisi pysyä jo valitussa AI:ssa pidempiä aikoja.
- Haluan varmistaa, että onko projektini laajuus riittävä tai tarpeeksi yhdenmukainen KPS-Markovin ketju paperin kanssa, jos tekoälyni toimii tässä raportissa kuvailemallani tavalla?

Projektiin käytetty aika tällä viikolla: 19h
