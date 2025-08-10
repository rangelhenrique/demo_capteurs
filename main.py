#Version 2.0
#Date : 2023-11-10
#Auteur : Henrique Rangel
#Description : Ici nous allons faire un pull request sur github

#Le but de ce programme est de generer des données aleatoires de plusieurs types de capteurs et les enregistrer dans un premier monment dans un format CSV et l'afficher dans le terminal
# Enregistrer le fichier est importat pour pouvoir faire des ameliorions continues dans le code (CI)

# Caracteristisques initiales du robot
# A) niveau de batterie | B) niveau de temperature | C) Position bidimensionelle

# étape 1 - Déclaration des libraries

import csv
import random
import time
from datetime import datetime

# étape 2 - Définition d'un fichier CSV pour lenregistrer les données

analyse_data = "donnees.csv"

#étape 3 - Nommer les variables à prendre la mesure

sortie = [
    "heure", "batterie(%)", "temperature(degrees)", "position_X", "position_Y"
]

#etape 4 - Création d'un fichier CSV
with open(analyse_data, mode="w", newline="") as fichier_sortie:
  writer = csv.writer(fichier_sortie)
  writer.writerow(sortie)

#etape 5 - Définir les valeurs aléatoires


def gen_donnees():
  heure = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
  batterie = random.randint(12, 100)
  temperature = round(random.uniform(30.0, 60.0), 1)
  position_X = round(random.uniform(0.0, 60.0), 1)
  position_Y = round(random.uniform(0.0, 60.0), 1)
  return [heure, batterie, temperature, position_X, position_Y]


#return [heure, batterie, temperature, position_X, position_Y]

#etape 6 - Démarrer la simulation (nous allons prendre 10 mesures)

for _ in range(10):
  donnees = gen_donnees(
  )  #les donnees seront enregistrees dans la liste gen_donees

  #etape 7 - Enregistrer les données dans le fichier CSV

  with open(analyse_data, mode="a", newline="") as fichier_sortie:

    writer = csv.writer(fichier_sortie)
    writer.writerow(donnees)

    #Etape 8 - Afficher les données dans le terminal

    print("log: ", donnees)

    #Etape 9 - Attendre 5 secondes avant de prendre la prochaine mesure
    time.sleep(1)
