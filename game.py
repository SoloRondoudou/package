from random import *


def loto(x, y):

    while True:
        """
        :param x: la valeur de x est un chois entre x et y
        :param y: la valeur de y est un chois entre x et y
        """
        print("le loto")

        choices = randint(x, y)

        val = int(input("donnee votre chiffre: "))

        print(choices)

        if (choices == val) :
            print("vous avez gagnée 1 000 000$")
        else:
           print("perdu")


def pierre_feuille_ciseau():

    while True:

        print("Bienvenue sur pierre feuille ciseaux")
        print("1 = pierre \n2 = feuille \n3 = ciseaux")

        chois = int(input("Quel est votre chois : "))
        random = randint(1, 3)

        if random == 1 and chois == 3:
            print("Vous avez perdue l'ordinateur a jouer la pierre")

        elif random == 3 and chois == 2:
            print("Vous avez perdue l'ordinateur a jouer le ciseau")

        elif random == 2 and chois == 1:
            print("Vous avez perdue l'ordinateur a jouer la feuille")

        elif random == chois:
            print("match nul")

        elif chois > 3:
            print("erreure... le chiffre est non valide !")

        else:
            print("vous avez gagner !")
