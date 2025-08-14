"""
Projet : Générateur & Journaliseur de données de capteurs (simulation) — logging + CLI
Version : 3.0.0
Module : robot_data_logger_cli.py
Description : Génère des mesures aléatoires (batterie, température, position XY),
              enregistre en CSV et utilise le logging. Accepte des arguments en
              ligne de commande pour définir la verbosité (INFO/DEBUG).
              

Auteur : Henrique RANGEL
Date : 2025-08-14
Python : >= 3.9
Dépendances : bibliothèques standards (csv, random, time, datetime, logging, argparse)

Notes :
- Noms des variables/fonctions/entrées/sorties préservés.
- E/S : écrit l'en-tête (w) une seule fois, puis garde l'ouverture en append pendant la boucle.
- Logs : logger.info remplace les impressions utilisateur ; logger.debug ajoute des détails.
- CLI : --debug (niveau DEBUG) ou --info (niveau INFO).
"""

# Version 2.1.1 - tester le GitHub

# Objectif : simuler des relevés de plusieurs types de capteurs et les enregistrer
# dans un fichier CSV, avec affichage optionnel via le système de logs.
# L'enregistrement structuré permet des améliorations continues (CI).
#
# Caractéristiques initiales du robot :
# A) niveau de batterie | B) niveau de température | C) position bidimensionnelle

# Étape 1 - Import des bibliothèques
import csv
import random
import time
import logging
import argparse
from datetime import datetime

# ---- Configuration du logging (silencieux par défaut) ----
logger = logging.getLogger("app")
if not logger.handlers:
    _handler = logging.StreamHandler()
    _fmt = logging.Formatter("[%(levelname)s] %(message)s")
    _handler.setFormatter(_fmt)
    logger.addHandler(_handler)
logger.setLevel(logging.WARNING)  # par défaut, pas de verbosité excessive

def set_debug(enabled: bool = True):
    """Active (DEBUG) ou désactive (WARNING) les journaux verbeux."""
    logger.setLevel(logging.DEBUG if enabled else logging.WARNING)

def set_info(enabled: bool = True):
    """Active (INFO) ou désactive (WARNING) les journaux d'information."""
    logger.setLevel(logging.INFO if enabled else logging.WARNING)

def dbg(msg: str, *args):
    """Compatibilité : utilise le backend logging pour les messages de debug."""
    logger.debug(msg, *args)

# Étape 2 - Définition du fichier CSV de sortie
analyse_data = "donnees.csv"

# Étape 3 - Noms des colonnes (en-têtes CSV)
sortie = [
    "heure", "batterie(%)", "temperature(degrees)", "position_X", "position_Y"
]

# Étape 4 - Création/initialisation du fichier CSV (écrit l'en-tête une seule fois)
with open(analyse_data, mode="w", newline="") as fichier_sortie:
    writer = csv.writer(fichier_sortie)
    writer.writerow(sortie)  # écriture de l'en-tête

# Étape 5 - Génération d'une ligne de mesures aléatoires
def gen_donnees():
    """Génère une liste représentant une mesure simulée.

    Retourne :
        list: [heure, batterie, temperature, position_X, position_Y]
    """
    # Horodatage local au format HH:MM:SS JJ-MM-AAAA
    heure = datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    # Batterie entre 12% et 100% pour éviter le 0% constant
    batterie = random.randint(12, 100)
    # Température et positions avec 1 décimale
    temperature = round(random.uniform(30.0, 60.0), 1)
    position_X = round(random.uniform(0.0, 60.0), 1)
    position_Y = round(random.uniform(0.0, 60.0), 1)
    return [heure, batterie, temperature, position_X, position_Y]

# Fonction principale : permet l'exécution avec arguments CLI
def main():
    # Analyse des arguments de ligne de commande
    parser = argparse.ArgumentParser(description="Simulation de capteurs avec journalisation.")
    parser.add_argument(
        "--debug", action="store_true", help="Active le niveau DEBUG (très verbeux)."
    )
    parser.add_argument(
        "--info", action="store_true", help="Active le niveau INFO (verbeux modéré)."
    )
    args = parser.parse_args()

    # Configuration du niveau de log selon les arguments reçus
    if args.debug:
        set_debug(True)
    elif args.info:
        set_info(True)

    # Étape 6 - Démarrer la simulation (nous allons prendre 10 mesures)
    # Optimisation : garder le fichier ouvert en mode append pendant toute la boucle
    with open(analyse_data, mode="a", newline="") as fichier_sortie:
        writer = csv.writer(fichier_sortie)

        for _ in range(10):
            # Génération d'une ligne de données
            donnees = gen_donnees()
            dbg("Données générées : %s", donnees)

            # Étape 7 - Écriture dans le CSV
            writer.writerow(donnees)
            logger.info("log: %s", donnees)

            # Étape 8 - Pause entre mesures pour simuler l'échantillonnage
            time.sleep(5)

            # Étape 9 - Message de version (debug uniquement)
            logger.debug("version 3.0")

# Point d'entrée du script
if __name__ == "__main__":
    main()
