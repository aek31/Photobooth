# Photobooth

A vérifier :
* witty pi 2 indique broche 11 utilisée, et le programmme aussi avec le raspberry, normal ? Modifier le schéma électrique et le tutorial partie numérique en conséquence
* rajouter clé USB sur le schéma électrique
* pour modifier programme : lancer photobooth, brancher un clavier, taper 'q' sur le clavier, le script se ferme et on a accès au bureau du Raspberry.



* Mettre une seule photo format bandeau (pas très grand en hauteur) avec de gauche à droite : face, arrière 3/4, 3210, intérieur, sur une table avec des gens qui l'utilisent (mariage Pauline)
* Mettre lien Youtube, 3 phases dans la vidéo : 1-Normal 2-Mode sombre 3-Fonctionnement très simple avec brnachement alim puis on/off puis ON raspberry avec indication flèches et textes superposés, défilement de plusieurs photos prises












* version raspbian, linux, python, bibliothèques codes, witty py soft

* Mettre lien vers le photobooth.py (explication du code ou tout dans les commentaires ?)

* dire de ne pas utiliser le même écran car on ne voit pas bien sur les côtés 

* IMPORTANT :dire qu'il faudra un ordinateur sous linux pour lire les photos stockées sur la clé USB

* Trouver une méthode, et l'expliquez, pour pouvoir lire de l'ext4 sous windows, voir par exemple : https://www.commentcamarche.net/forum/affich-13495573-lire-ext4-sous-windows



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
