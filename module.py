"""
cote main.py :


import test    // importer le fichier module

test.lol()     // utiliser la fontion


cote modules.py

def lol():
  print("c'est tros drole 🤣")

"""

"""
    database
db["yann"] = "13"   cree une cle dans la base de donne yann -> 13
  print(db["yann"])   afficher la valeur de la cle yann
  matches = db.prefix("yann")  lister une cle
  print(matches)
  del db["yann"]      supprimer la cle yann
"""

import time
import random
import matplotlib.pyplot as plt


def delay(x):
    """
    :param x: l'elemen x serre a attendre "x" seconde(s)
    """
    time.sleep(x)


def graphique(liste):
    plt.plot(liste)
    plt.show()


def modules():
    print("patientier le module se charge")
    print("si une erreur se produit c'est normal merci d'attendre")
    help('modules')
    exit()


def module():
    nom_du_module = input("Quel est le nom du module : ")
    print("patientier les modules se charge")
    help(nom_du_module)
    exit()
