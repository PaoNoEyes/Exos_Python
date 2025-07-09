



from random import randint
import os


def jeu():
    nom_joueur = input("rentrez votre nom pour les highscores :\n")
    rand = randint(1,10)
    compt = 0
    score = 100
    gagné = False
    while compt != 10 and gagné == False:
        user = int(input("choisissez un nombre entre 1 et 10\n"))
        if user == rand:
            print("bien joué !\n")
            gagné = True
        else : 
            print("essaie encore\n")
            score = score - 10
            compt = compt + 1
    a = "\n"+str(nom_joueur)+" a fini le jeu avec "+str(score)+" points"
    return a

def Afficher_points(file):
    
    fichier_a_ouvrir = open(file,"r")
    contenu_du_fichier = fichier_a_ouvrir.read()
    print(contenu_du_fichier)
    fichier_a_ouvrir.close()

def Ajouter_score(file,ajout):
    
    with (open(file,'a')) as fichier_a_remplir:
        fichier_a_remplir.write(ajout)


def programme():
    file_path = os.getcwd()
    print(file_path)
    file = ""                                                                               #/!\ mettez ici le chemin de votre result.txt
    continu = True
    while continu == True:
        Ajouter_score(file,jeu())
        a = input("Voulez vous afficher les scores ? y/n")
        if a == "y":
            Afficher_points(file)
        b = input("Voulez vous rejouer ? y/n")
        if b == "n":
            continu = False

programme()
