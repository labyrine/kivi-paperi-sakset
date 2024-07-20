## Viikkoraportti 2

Toisella viikolla virkistin muistiani projektista. Luin markovin ketjusta uudestaan, että muistaisin miten se toimii ja voisin verrata sitä omaan projektiini, koska olin unohtanut aika paljon. Luin myös kurssiaikataulun.

Selvittelin, mikä voisi olla ongelmana tekoälyn toiminnassa ja löysin, että merkkijono last_seven (joka sisältää viimeiset 7 pelaajan valintaa) ei päivittynyt oikein. Sen vuoksi tekoäly valitsi aina randomisti oman valintansa, eikä käyttänyt eri tekoälyjä 1-6 lainkaan. Eli korjasin sen ongelman. 

Löysin bugin, jossa AI valitsi tyhjän merkkijonon. Tämä johtui siitä, että AI:den pisteytys plussaamalla ja miinustamalla voittojen ja häviöiden mukaan antaa AI:lle mahdollisuuden valita “parhaaksi” AI:ksi sellaisen, jolla ei ole olemassa ennustuksia haluttuun tilanteeseen. Tällä hetkellä se on korjattu antamalla algoritmin valita siinä tilanteessa k, p tai s randomisti. Minun pitää miettiä jossain välissä, että, olisiko siihen olemassa parempi vaihtoehto vai onko nykyisellä ratkaisulla väliä enää, kun alan käyttämään useampia kierroksia.

Kirjoitin AI:t 1-6 kompaktimmin ja lisäsin pelin loppuun AI:n voittoprosentin sekä kaikkien AI:den pisteytykset pelin lopusta. Lisäsin myös jokaisen kierroksen jälkeen tyhjän rivin pelin lukemisen helpottamiseksi. 

Seuraavalla viikolla alan testaamaan projektiani mm. löytääkseni bugeja. En ole vielä varma miten sitä kannattaa testata kokonaisuudessaan, mutta kysyn ohjaajilta, jos jään jumiin. Samalla minun kannattaa lisätä pelikierrosten määrää ja aloittaa testausten dokumentointi. Aion myös käydä läpi pylint virheitä. 

Pidemmällä aikavälillä haluan testata algoritmini toimivuutta ja parannella sitä, kunhan saan vielä mahdolliset virheet pois.

Käytin aikaa projektiin aikaa tällä viikolla 11 tuntia.
