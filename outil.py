from statistics import *
import time
import random
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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


def piaire(rayon):
    pi = 3.14159265358979323846264338327950288419716939937510582
    ryoncarre = rayon * rayon
    result = pi * ryoncarre
    print("l'aire de ce cercle est ", result)


def lettre_min():
    min = "abcdefghijklmnopqrstuvwxyz"
    return min


def lettre_maj():
    maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return maj


def caractere_special():
    spe = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    return spe


def chiffre():
    chi = "0123456789"
    return chi


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

    elif read_or_write == "r":

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


def ia(valeur_entrer, donne_sortie, inputSize, hiddenSize, outputSize, train):
    x_entrer = np.array(valeur_entrer, dtype=float) # données d'entrer
    y = np.array(donne_sortie, dtype=float) # données de sortie /  1 = rouge /  0 = bleu

    # Changement de l'échelle de nos valeurs pour être entre 0 et 1
    x_entrer = x_entrer / np.amax(x_entrer, axis=0) # On divise chaque entré par la valeur max des entrées

    # On récupère ce qu'il nous intéresse
    X = np.split(x_entrer, [len(x_entrer) - 1])[0] # Données sur lesquelles on va s'entrainer, les 8 premières de notre matrice
    xPrediction = np.split(x_entrer, [len(x_entrer) - 1])[1] # Valeur que l'on veut trouver

    #Notre classe de réseau neuronal
    class Neural_Network(object):
        def __init__(self):
                
        #Nos paramètres
            self.inputSize = inputSize # Nombre de neurones d'entrer
            self.outputSize = outputSize# Nombre de neurones de sortie
            self.hiddenSize = hiddenSize # Nombre de neurones cachés

        #Nos poids
            self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (2x3) Matrice de poids entre les neurones d'entrer et cachés
            self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) Matrice de poids entre les neurones cachés et sortie


        #Fonction de propagation avant
        def forward(self, X):

            self.z = np.dot(X, self.W1) # Multiplication matricielle entre les valeurs d'entrer et les poids W1
            self.z2 = self.sigmoid(self.z) # Application de la fonction d'activation (Sigmoid)
            self.z3 = np.dot(self.z2, self.W2) # Multiplication matricielle entre les valeurs cachés et les poids W2
            o = self.sigmoid(self.z3) # Application de la fonction d'activation, et obtention de notre valeur de sortie final
            return o

        # Fonction d'activation
        def sigmoid(self, s):
            return 1/(1+np.exp(-s))

        # Dérivée de la fonction d'activation
        def sigmoidPrime(self, s):
            return s * (1 - s)

        #Fonction de rétropropagation
        def backward(self, X, y, o):

            self.o_error = y - o # Calcul de l'erreur
            self.o_delta = self.o_error*self.sigmoidPrime(o) # Application de la dérivée de la sigmoid à cette erreur

            self.z2_error = self.o_delta.dot(self.W2.T) # Calcul de l'erreur de nos neurones cachés 
            self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # Application de la dérivée de la sigmoid à cette erreur

            self.W1 += X.T.dot(self.z2_delta) # On ajuste nos poids W1
            self.W2 += self.z2.T.dot(self.o_delta) # On ajuste nos poids W2

        #Fonction d'entrainement 
        def train(self, X, y):
                
            o = self.forward(X)
            self.backward(X, y, o)

        #Fonction de prédiction
        def predict(self):
                
            #print("Donnée prédite apres entrainement: ")
            #print("Entrée : \n" + str(xPrediction))
            #print("Sortie : \n" + str(self.forward(xPrediction)))

            if(self.forward(xPrediction) < 0.5):
                return 0
            else:
                return 1


    NN = Neural_Network()

    for i in range(0, train): #Choisissez un nombre d'itération, attention un trop grand nombre peut créer un overfitting !
        #print("# " + str(i) + "\n")
        #print("Valeurs d'entrées: \n" + str(X))
        #print("Sortie actuelle: \n" + str(y))
        #print("Sortie prédite: \n" + str(np.matrix.round(NN.forward(X),2)))
        #print("\n")
        NN.train(X,y)

    return NN.predict()

def casino(defaultcompte, personne, nombretentative, pourcentage, z):
    print()
    meanliste = []
    defaultmise = defaultcompte / (nombretentative * personne)
    for i in tqdm(range(0, z), desc ="Chargement"):
        mise = defaultmise
        listegain = []
        i = 0
        for y in range(0, personne):
            mise = defaultmise
            compte = defaultcompte
            i = 0
            for y in range(0, nombretentative):
                mise = defaultmise
                compte = defaultcompte
                i = 0
                while i < nombretentative or compte < (defaultcompte + 1) :
                    compte = compte - mise # on mise 2 €
                    x = random.randint(1, 2)      # la roue tourne

                    if x == 2 :
                        mise = mise * 2    # on re-mise le double  
                        i = i + 1

                    elif x == 1:
                        gain = mise * 2 # on multiplie la mise
                        compte = compte + gain # on ajoute le gain au compte
                        mise = defaultmise # on re-mise 2€
                        i = i + 1
            gaingeneral = compte - defaultcompte
            listegain.append(gaingeneral)

        resultat = sum(listegain)
    
        x = resultat
        meanliste.append(x)

    resultatgeneral = sum(meanliste) / len(meanliste)
    argentpourtoi = pourcentage * resultatgeneral / 100
    argentpourlesautre = (resultatgeneral - argentpourtoi) / personne
    pourcentagecompte = 100 * resultatgeneral / defaultcompte
    foisx = 1 + (pourcentagecompte / 100)
    listeresultat = []
    for i in range(0, z):
        listeresultat.append(resultatgeneral)
    print("\nen moyenne sur", str(z), "tests avec", str(nombretentative), "mises pour", str(personne), "personnes on obtient un gain de", str(resultatgeneral), "€")
    print("pour vous cela  fera", str(argentpourtoi),"€ et pour les", str(personne),"personne cela fera", str(argentpourlesautre),"€ pour chacune")
    print("ce qui fait donc", str(pourcentagecompte) + "%", "de de comte de départ sois un ×" + str(foisx),)
    print("Dans le meilleur des cas on a un bénéfice de", str(max(meanliste)), "€ et dans le pire un bénéfice de", str(min(meanliste)), "€\n")
    plt.grid(True)
    plt.plot(meanliste, linewidth=2)
    plt.plot(listeresultat, linewidth=4)
    plt.show() # affiche la figure à l'écran
