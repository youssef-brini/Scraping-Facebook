# Scraping Facebook
## Prérequis
#### assurez-vous que vous avez déjà installé le chrome driver :
   vous pouvez utiliser ce lien "https://chromedriver.chromium.org/downloads"
#### Configurer votre paths :
 * chrome driver : fichiers(script_scrap_comment.py , script_scrap_fb.py , script_scrap_post.py )
 * test.csv : fichier ( configuration_file.py )
 * configuration fb : fichiers dans la methode login (script_scrap_comment.py , script_scrap_fb.py , script_scrap_post.py)
#### configurer votre compte Facebook :
   entrer votre adresse et mot de pass dans le fichier "Configurations_fb.txt"
#### Afin de pouvoir exécuter l'application, vous devez d'aborder installer les dépendances suivantes :
  * pymongo
  * datetime
  * hashlib
  * selenium
  * bs4
  * flask
  * flask_restful
 
### Installation
1. Ouvrir une invite de commande
2. taper : pip install "nom du bibliothèque" .
 
## Exécution
* Post Scraping
   1. remplir le fichier "test.csv" par les URLs des posts que vous voulez scrappé  
   2. ouvrire le projet sur votre Editeur
   3. Exécuter le fichier "api_facebook_scrap_post.py"
   4. Ouvrir une invite de commande et aller sur l'emplacement du projet ( cd /path )
   5. Exécuter le fichier "ipost.py" (py ipost.py)
* Page Scraping
   1. ouvrire le projet sur votre Editeur
   2. remplire la liste « liste_urls » dans le fichier api_facebook_scrap par les urls des pages facebook que vous souhaitez scrappez 
   3. exécuter le fichier "api_facebook_scrap.py"
   4. connecter sur le lien " http://127.0.0.1:5000/api/scraping"
   