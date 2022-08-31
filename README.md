# P8 Créez une plateforme pour amateurs de Nutella

*L'application permet à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop salé".*

## Pour commencer

### Pré-requis

Ce qu'il est requis pour commencer...

* Python 3 *https://www.python.org/downloads/*
* PostgreSQL *https://www.postgresql.org/download/*
* Git *https://git-scm.com/downloads*
* GitHub *https://github.com/*
* Un éditeur de code (ici PyCharm est utilisé *https://www.jetbrains.com/pycharm/download/download-thanks.html*)

### Installation


Dans votre terminal, clonez le package avec git sur votre dépôt local (ordinateur) comme ceci:
 - Etape 1 : initialisation de git dans le dossier correspondant avec: *`git init`*
 - Etape 2: *`git remote add <nom du fichier> https://github.com/KlereBibi/P8_PurBeurre_.git`* 
 - Etape 3: *`git clone https://github.com/KlereBibi/P8_PurBeurre_.git`*
 
Toujours dans le terminal, initialisez votre environnement virtuel:
 - Etape 1: installation de pipenv avec la commande: *`pip install pipenv`*
 - Etape 2: initialisation de l'environnement virtuel dans le package: *`pipenv shell`* 
 - Etape 3: installer les modules nécessaires grâce au fichier requierements.txt: *`pipenv install -r requirements.txt`*

## Démarrage
* Ouvrez un terminal dans le dossier de l'application 
* Tappez python manage.py migrate
* Tappez python manage.py makemigration
* Tappez python manage.py collectstatic
* Tappez python manage.py runserver pour lancer l'application
* Appuyez sur la touche CTRL + click souris sur le lien http pour ouvrir l'application

## Fabriqué avec
* PyCharm - Editeur de texte

## Versions
* python 3.9.1
* Django 4.0.6

## Auteur

Claire Biedermann


## Auteur
Claire Biedermann
