# Photobooth

A vérifier :
* witty pi 2 indique broche 11 utilisée, et le programmme aussi avec le raspberry, normal ? Modifier le schéma électrique et le tutorial partie numérique en conséquence
* rajouter clé USB sur le schéma électrique
* pour modifier programme : lancer photobooth, brancher un clavier, taper 'q' sur le clavier, le script se ferme et on a accès au bureau du Raspberry.





<img src="https://github.com/aek31/Photobooth/blob/master/Photos/trois.JPG" alt="drawing" height="150px"/>           <img src="https://github.com/aek31/Photobooth/blob/master/Photos/deux.JPG" alt="drawing" height="150px"/>  <img src="https://github.com/aek31/Photobooth/blob/master/Photos/un.JPG" alt="drawing" height="150px"/>  <img src="https://github.com/aek31/Photobooth/blob/master/Photos/zero.JPG" alt="drawing" height="150px"/> 


Vous voulez faire votre propre photobooth, cette page est faite pour vous !





| POINTS CLES DU PHOTOBOOTH|     
| :-------------------------------------  | 
| Monobloc : juste un câble secteur à brancher et tout fonctionne !    |
| On récupère les photos en récupérant la clé USB dans le photobooth     |
| Bonne qualité des photos, voir ici des photos prises en mariage et en anniversaire    |
| Fonctionne dans une pièce très sombre comme une salle de danse, pas besoin d'éclairage externe    |
| Personnalisation du texte affiché quand la photo est prise (ex : Chic Guinguette Chic -  30 ans), ce texte ne sera pas visible dans les photos finales    |

| SOMMAIRE |     
| :-------------------------------------  |  
| 1- Tutorial d'installation de la partie numérique     |
| 2- Fabrication de l'éclairage      |
| 3- Câblage alimentation secteur      |
| 4- Fabrication de la boîte      |
| 4- Ma méthode étape par étape      |




* Mettre une seule photo format bandeau (pas très grand en hauteur) avec de gauche à droite : face, arrière 3/4, 3210, intérieur, sur une table avec des gens qui l'utilisent (mariage Pauline)
* Mettre lien Youtube, 3 phases dans la vidéo : 1-Normal 2-Mode sombre 3-Fonctionnement très simple avec brnachement alim puis on/off puis ON raspberry avec indication flèches et textes superposés, défilement de plusieurs photos prises





### Tutorial d'installation de la partie numérique
------
| Elements nécessaires (version/modèle)   |      Rôle     | 
| :-------------------------------------  | :------------- | 
| Raspberry Pi avec carte SD 16Go      |Contient le logiciel photobooth.py|
| Pi Camera avec rallonge 1 mètre                       |Filme et prend les photos, rallonge nécessaire car le câble d'origine ne fait que 10 cm     |    
| Carte Wiring Pi                  |- Eteindre proprement le raspberry après l'appui sur le bouton poussoir |     
|                                  |- Sauvegarder l'heure et la date quand le raspberry est hors tension grâce à sa pile (intérêt : dater les photos)   |         
| Ecran de PC (Dell + réf)         |Afficher la scène et voir la photo prise pendant quelques secondes     |     
| Gros bouton rouge                |Un appui est le décompte commence      |       
| Clé USB  32Go                        |Les photos sont stockées sur une clé USB      | 


Méthode  :    
1° sur un table faire toute fonctionner    
2° fabriquer la boîte du photobooth
3° tout intégrer




_______
1. Installation du Raspberry Pi
* Télécharger Raspbian (système d'explitation du Raspberry Pi) sur votre PC : https://www.raspberrypi.org/downloads/raspbian/
* Copiez Raspbian sur une carte SD (attention, choisissez la procédure adaptée à votre système d'exploitation) : https://www.raspberrypi.org/documentation/installation/installing-images/README.md
* Mettre la carte SD dans le raspberry PI et relier l'écran par le câble HDMI au raspberry
* Brancher le câble d'alimentation du raspberry Pi, si tout fonctionne le système d'exploitation Raspbian démarrer à l'écran
* Suivre les étapes d'installation (si besoin cherchez un tutorial pour vous aider)
* Une fois l'installation terminée configurez le wifi pour avoir accès à internet : https://www.digikey.com/en/maker/blogs/raspberry-pi-3---how-to-connect-wi-fi-and-bluetooth
* Mettre à jour Raspbian :  
```
sudo apt-get install
sudo apt-get upgrade
```
_______
 2. Faire fonctionner la pi Camera avec sa ralonge : 
* Déclipseer vers le haut le conecteur de la pi Camera pour enlevé le câble d'origine
* Inséré le nouveau câble de 1 mètre puis clipsé vers le bas le connecteur de la pi Camera pour fixer le câble
* Déclipsé le connecteur du raspberry pi puis insérer le câble de la pi Camera
* Clipsé le connecteur du Raspberry
* Suivre le tutorial suivant pour tester que votre caméra fonctionne bien : https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/4 
##### A ce stade vous avez une caméra qui fonctionne, vous êtes prêt à transformer votre raspberry en photobooth !
_______
3. Câbler un bouton poussoir au raspberry Pi :
* relier les deux broches d'un bouton poussoir aux broches suivantes du raspberry : GPIO17 (broche 11) et GND (broche 6)
_______
ATTENTION : est-ce qu'il faut télécharger le programme sous github pour être sur de toujours l'avoir ?

4. Installer la carte Witty Pi
* plugger la carte Witty Pi sur la carte Raspberry Pi
* mettre la pile CR2032 sur la carte Witty Pi
* laisser tous les cavaliers dans la position d'origine
* mettre le câble d'alimentation du raspberry sur le port micro usb de la carte Witty Pi. Désormais c'est la carte Witty Pi qui alimentera le raspberry Pi.
* cliquer sur le bouton ON/OFF de la carte Witty Pi, le raspberry va démarrer comme d'habitude sur votre évran
* ouvrir un terminal puis tapez :
```
pi@raspberrypi $ cd ~
pi@raspberrypi ~ $ wget http://www.uugear.com/repo/WittyPi2/installWittyPi.sh
pi@raspberrypi ~ $ sudo sh installWittyPi.sh
pi@raspberrypi ~ $ cd wittyPi
pi@raspberrypi ~ /wittyPi $ ls
daemon.sh init.sh syncTime.sh runScript.sh utilities.sh wittyPi wittyPi.sh
```
* Vérifiez qu'après la commande ls vous avez bien les 7 fichiers ci-dessus
* Réglez l'heure et la date sur le raspberry
* On va tranférer l'heure du raspberry pi sur la carte Wiring Pi, ouvrez un terminal et tapez :

```
pi@raspberrypi ~/wittyPi $ sudo ./wittyPi.sh 
```
* Tapez le chiffre 1
* Tapez le chiffre 8
* Eteignez le raspberry Pi par l'interface
* Appuez sur le bouton ON/OFF de la carte Wiring Pi, vérifier que l'heure et la date sont correctes à l'écran
* Câbler un bouton poussoir sur les broches Switch et GND
* Mettre photo
* Désormais vous allumerez votre raspbeery à l'aide de ce bouton


_______
5. Copiez le logiciel photobooth.py :
_______
4. Installer bibliothèques
7. Lancer le logciciel à chaque démarrage





* version raspbian, linux, python, bibliothèques codes, witty py soft

* Mettre lien vers le photobooth.py (explication du code ou tout dans les commentaires ?)

* dire de ne pas utiliser le même écran car on ne voit pas bien sur les côtés




* Points d'amélioration : chargement photo par WIFI ou bloothooth, récupérer dernière photo sur son téléphone, récupérer ses photos sous Windows ou Mac os




### Eclairage
------

* Trois bandeaux à led en forme de "U"  fixés sur une planche
* Un plexiglas découpé en forme de "U" pour atténuer la lumière des leds
* La planche avec les bandeaux à leds 20 cm derrère le plexiglas (trop proche ca aveugle, trop loin ca n'éclaire pas assez)
* Outils utilisés : dremmel avec type de lame pour découpe du plexiglas

#### Des photos visibles même dans une salle très sombre (par exemple une salle de danse) 
Bandeau à leds            |   Plexiglas découpé et fixé par des vis
:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/bandeau_leds.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/plexi.jpg" alt="drawing" height="250px"/>


Bandeau à l'intérieur du photobooth           |    
:-------------------------:|
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/eclairage_dedans.JPG" alt="drawing" height="250px"/> 







### Câblage électrique
------
Voir le schéma électrique ici 

#### Partie secteur (partie dangereuse !)
* Mettre photo vue de dessus avec capôt boîte de dérivation ouverte
* Attention : prendre bouton et voyant qui supporte 230V et 1A minimum
* En ouvrant la boîte aucun cuivre avec du 230V ne peut être touché donc utilisation de beaucoup de gaine thermo, boîte de dérivation, ...
* Photos des différents éléments protecteurs

#### Partie 12V et 5V
* Règle : pouvoir enlever chaque élément sans dessouder dans la boîte donc des connecteurs et dominos
* prendre photo domini porte gauche et connecteurs x 2 proche de la boîte


### Fabrication de la boîte
------
* L'écran Dell est un écran de récupération et est vraiment lourd ! 
* La principale difficulté était donc de faire une boîte suffisament solide pour maintenir l'écran plat à la verticale
* Du coup le photobooth est lourd, grand et difficile à manipuler, notamment pour le rentrer dans une voiture. J'ai donc mis deux poignées de chaque côté.
* Pour fixer l'écran deux barres fixées par quatre équerres et deux équerres en haut et bas pour maintenir l'écran fixe dans toutes les positions
* Outils utilisés : scie sauteuse, scie, appareil pour augmenter profondeur trous, cales, ...
* Expliquer la peinture, d'abord sosu-couche puis peinture à bois
* Normalement 3 couches mais par manque de temps je n'en ai mis qu'une seule


* Voici quelques étapes de la construction :



1- Préparation découpe face avant    |   2- Découpe avant  |   3- Fixation écran
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/position_face_avant.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/decoupe_face_avant.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/3fixation_ecran1.jpg" alt="drawing" height="250px"/> 


4- Face arrière + porte     |   5- Ajout des côtés  |   6- Ajout face avant |   7- Peinture
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/5porte.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/7côtés.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/8ajout_face_avant.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/9_peinture_avant.jpg" alt="drawing" height="250px"/> 


8- Deux améliorations pour le rentrer dans une voiture : quatre poignées pour le soulever à l'horizontale et cinq surrélévations    |   9- Les surrélévations protègent les boutons quand il est posé sur le dos (dans une voiture)  |   
:-------------------------:|:-------------------------:|
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/poignées.JPG" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/protection_voiture.JPG" alt="drawing" height="250px"/> 


### Ma méthode étape par étape 
------
| Ma méthode pour réaliser votre photobooth étape par étape  |     
| :-------------------------------------  |  
| 1- Rassembler tout le matériel numérique (raspberry, écran de PC, carte wiring Pi, ...)     |
| 2- Faire fonctionner tout ce matériel numérique sur table     |
| 4- Sur une table faire fonctionner l'éclairage et voir le résultat en mettant la caméra et le plexiglas par desssus      |
| 5- Fabriquer la boîte et découper le pléxiglas      |
| 6- Intégrer le numérique dans la boîte      |





| Titre 1       |     Titre 2     |        Titre 3 |
| :------------ | :-------------: | -------------: |
| Colonne       |     Colonne     |        Colonne |
| Alignée à     |   Alignée au    |      Alignée à |
| Gauche        |     Centre      |         Droite |


```
Give the example
```
