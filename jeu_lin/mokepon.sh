#!/bin/bash

echo Lancement de votre jeu
echo Afin d'avoir la possibilite de jouer a notre jeu faites en sorte d'avoir les droits d'administrteur sur votre machine ou demandez la permission a votre administrateur systeme.

echo L'installation de python 3.8.7 va commencer sur votre machine.
sudo apt-get update
sudo apt-get install python3.8.7

python jeu.py

quit
