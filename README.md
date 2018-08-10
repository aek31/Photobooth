# Photobooth

### Présentation
------
Vous voulez faire votre propre photobooth, cette page est faite pour vous !
* Mettre une seule photo format bandeau (pas très grand en hauteur) avec de gauche à droite : face, arrière 3/4, 3210, intérieur, sur une table avec des gens qui l'utilisent (mariage Pauline)
* Mettre lien Youtube
* 3 phases dans la vidéo : 1-Normal 2-Mode sombre 3-Fonctionnement très simple avec brnachement alim puis on/off puis ON raspberry avec indication flèches et textes superposés
* Lien vers dossier avec photos prises par le photobooth
### Fonctionnement
------

* Schéma électrique + lumière + clé USB de tout le photobooth
* expliquer comment on récupère lesphotos
* A poser sur une une table
### Tutorial d'installation du logiciel
------
| Elements nécessaires (version/modèle)   |      Rôle     | 
| :-------------------------------------  | :------------- | 
| Raspberry Pi                     |Contient le logiciel photobooth.py|
| Pi Camera                        |Filme et prend les photos     |    
| Carte Wiring Pi                  |- Eteindre proprement le raspberry après l'appui sur le bouton poussoir |     
|                                  |- Sauvegarder l'heure et la date quand le raspberry est hors tension grâce à sa pile (intérêt : dater les photos)   |         
| Ecran de PC (Dell + réf)                     |Afficher la scène et voir la photo prise pendant quelques secondes     |     
| Gros bouton rouge                |Un appui est le décompte commence      |       
| Clé USB                          |Les photos sont stockées sur une clé USB      | 

* Principale difficulté : suppertoser les décompte (3,2,1,...) à l'image filmée

1. Télécharger Raspbian
2. Mettre à jour Raspbian 
4. Installer bibliothèques
5. Installer caméra 
6. Installer logiciel Witty Pi
6. Copier le logiciel
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
Bandeaux à leds            |   Plexiglas découpé et fixé par des vis
:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/bandeau_leds.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/plexi.jpg" alt="drawing" height="250px"/>








### Electrique 230V
------

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



1- Mesures trous face avant    |   2- Découpe avant  |   3- Fixation écran
:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/position_face_avant.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/decoupe_face_avant.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/3fixation_ecran1.jpg" alt="drawing" height="250px"/> 


4- Face arrière + porte     |   5- Ajout des côtés  |   6- Ajout face avant |   7- Peinture
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="https://github.com/aek31/Photobooth/blob/master/Photos/5porte.jpg" alt="drawing" height="250px"/> |          <img src="https://github.com/aek31/Photobooth/blob/master/Photos/7côtés.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/8ajout_face_avant.jpg" alt="drawing" height="250px"/> | <img src="https://github.com/aek31/Photobooth/blob/master/Photos/9_peinture_avant.jpg" alt="drawing" height="250px"/> 



| Titre 1       |     Titre 2     |        Titre 3 |
| :------------ | :-------------: | -------------: |
| Colonne       |     Colonne     |        Colonne |
| Alignée à     |   Alignée au    |      Alignée à |
| Gauche        |     Centre      |         Droite |


```
Give the example
```
