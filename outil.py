from tkinter import *
from statistics import *
import time
import random


def tkinter(titre, taill, min_x, min_y, color, logo):
    """
    :param titre: l'element titre vous servira a donner un titre a votre page (cette element doit etre ecrit entre "" ex: "titre")
    :param taill: l'element taill vous servira a definir une taill (cette element doit etre ecri entre "" ex: "360x360")
    :param min_x: l'element  vous servira a definir la plus petite tail en x (cette element doit etre ecri sans "" ex: 360)
    :param min_y: l'element  vous servira a definir la plus petite tail en y (cette element doit etre ecri sans "" ex: 360)
    :param color: l'element  vous servira a definir la couleur de font (cette element doit etre ecri entre "" ex: black ou #FF0000)
    :param logo: l'element  vous servira a definir  un petit logo en haut a gauche (cette element doit etre ecri entre "" ex: "logo.ico")
    """
    windows = Tk()
    windows.title(titre)
    windows.geometry(taill)
    windows.minsize(min_x, min_y)
    windows.config(background=color)
    windows.iconbitmap(logo)
    windows.mainloop()


def code(code):
    """
    :param code: l'element code sera le code que vou aller choisir (cette element doit etre ecri entre "" ex : "200ET"
    """
    code_v = input("code : ")
    code_valide = len(code_v)
    if code_v == code:
        print("code bon")
        code_validation = input("confirmer votre code : ")
        if code_validation == code:
            print("vous etes inscris")


        else:
            print("recomencer mauvais code")
            recommencer = input("je ne connais pas le mot de passe (appuis sur une touche) : ")
            if recommencer != 1:
                nom = input("quel est votre nom : ")
                if nom == "yann":
                    print("ok")
                    nomf = input("quel est votre nom de famille : ")
                    if nomf == "guszkiewicz":
                        print("vous etes inscris")

    else:
        recommencer = input("je ne connais pas le mot de passe (appuis sur entrer) : ")
        if recommencer != 1:
            nom = input("quel est votre nom : ")
            if nom == "yann":
                print("ok")
                nomf = input("quel est votre nom de famille : ")
                if nomf == "guszkiewicz":
                    print("vous etes inscris")


def gramme_en_ml(gramme):
    """
    :param gramme: l'element gramme pourra convertire les grammes en ml de lait
    """
    result = gramme * 1.03
    print(result, "ml de lait")


def ml_en_gramme(ml):
    """
     :param ml_en_gramme: merci de vous rendre a la fontion gramme_en_ml
    """
    result = ml / 1.03
    print(result, "gramme")


def moyenne(liste):
    moyenne = mean(liste)
    print(moyenne)


def aleatoir_nbr(x, y):
    """
    :param x: la valeur de x est un chois entre x et y
    :param y: la valeur de x est un chois entre x et y
    """
    choices = random.randint(x, y)
    print(choices)


def aleatoir(x):
    choices = random.choice(x)
    print(choices)


def timer():
    """
    :return: cette fontion serre a cree un timmer
    """
    for u in range(100):
        y = input("timmer : ")
        y = int(y)
        y = y + 1
        for x in range(0, y):
            print(x, "seconde")
            time.sleep(1)

        print("temps termine")
        print("")
        print("")
        print("")
        print("")
        print("")

    print("appuyer sur run")


def addition(x, y):
    result = x + y
    print(result)


def soustration(x, y):
    result = x - y
    print(result)


def division(x, y):
    result = x / y
    print(result)


def multiplication(x, y):
    result = x * y
    print(result)


def affiche(x):
    """
    :param x: l'elemen x serre a ecrire quelque chose sur la console
    """
    print(x)


def vitesse(km, h):
    result = km / h
    print("Vous allez a " + str(result) + "km/h")

def piperimetre(diametre):
    pi = 3.14159265358979323846264338327950288419716939937510582
    perimetre = pi * diametre
    print("le perimetre est ", perimetre)


def pidiametre(perimetre):
    pi = 3.14159265358979323846264338327950288419716939937510582
    diametre = perimetre / pi
    print("le diametre est ", diametre)


def vetement():
    print("voici le chois de vetement de cette journer\n")
    habit_tete = ["un collier", "des boucles d'oreilles", "une casquette", "des lunettes", "bracelet"]
    habit_haut = ["un T-shirt manche longue", "un T-shirt manche courte", "un pulle"]
    habit_bas = ["un pantalons", "une jupe", "une salopette", "un shirt"]
    couleur = ["blanc(he)", "noir", "rose", "bleu", "gris(e)", "jaune"]

    print(random.choice(habit_tete), random.choice(couleur))
    print(random.choice(habit_haut), random.choice(couleur))
    print(random.choice(habit_bas), random.choice(couleur))


def timer_minute(x):
    for i in range(0, x):
        print(i, "minute")
        time.sleep(15)
        print(i, ". 25 minute")
        time.sleep(15)


        print(i, ". 50 minute")
        time.sleep(15)
        print(i, ". 75 minute")
        time.sleep(15)


def fichier():
    read_or_write = input("lire(r) ecrire(w) : ")

    fichier = input("nom du fichier : ")

    if (read_or_write == "w"):
        x = input()

        with open(fichier, "w+") as fichier:
            fichier.write(x)

        fichier.close()
        print("fichier cree")


    elif (read_or_write == "r"):
        with open(fichier, "r") as fichier:
            i = fichier.read()
            print("voici la lecture : ")
            print("")
            print(i)


def Tableau():
    liste = []
    print("1 = ajouter 1 element")
    print("2 = ajouter plusieurs elements")
    print("3 = supprimer")
    print("4 = afficher")
    print("5 = tout supprimer")
    print("6 = nombre d'article")
    print("7 = quitter")
    while (1 == 1):
        print("")
        action = input("ation : ")

        if (action == "1"):
            aj = input("que voulez vous ajouttez : ")
            liste.append(aj)
            print(aj, " a ete ajouter a : ", liste)
            print("")



        elif (action == "2"):
            article = input("merci de separer les element par une virgule ex : oeufs,eau,... : ").split(",")
            liste.extend(article)
            print(article, "ont ete ajouter a la liste")
            print("voici la liste : ", liste)
            print("")




        elif (action == "6"):
            compte = len(liste)
            print("il y a : ", compte, " element(s)")
            print("")



        elif (action == "4"):
            print("voici votre list : ", liste)
            print("")


        elif (action == "3"):
            personage = input("le quel voulez vous supprimer : ")
            liste.remove(personage)
            print(personage, "a ete supprimmer")
            print("list : ", liste)
            print("")




        elif (action == "5"):
            liste.clear()
            print("tout a ete effacer : ", liste)
            print("")



        elif (action == "7"):
            print("au revoir")
            quit()


        else:
            print("action non valide")
