
from random import randint


def confectionner_une_liste(liste1):
    x=input("longueur de la liste :")
    for i in range(int(x)):
        liste1.append(randint(0,100))
    return liste1

def croissant_ou_decroissant(liste1):
    croiss = ""
    while croiss != False and croiss != True:
        croiss = input("croissant (c) ou decroissant (d) ?")
        if croiss == "c":
            croiss = False
        elif croiss == "d":
            croiss = True
        else:
            return "mets un des 2 choix bordel"
    liste1.sort(reverse=croiss)
    return liste1


def trouver_index(liste1):
    valeur = int(input("quelle est la valeur à rechercher:"))
    if valeur in liste1:
        print("trouvé")
        index=[u for u, x in enumerate(liste1) if x==valeur]
        return index
    else :
        return "la valeur n'est pas dans la liste"


choix=1
liste2=[]

while choix==1 or choix==2 or choix==3 or choix==4:

    choix= int(input("selectionner un choix : \n"
          "1: créer une liste simple \n"
          "2: ranger la liste créé dans le 1 \n"
          "3: trouvé la place d'une valeur dans la liste créer \n"
          "4: Quitter \n"))
    if choix==1:
        print(confectionner_une_liste(liste2))
        input()
    elif choix==2:
        print(croissant_ou_decroissant(liste2))
        input()
    elif choix==3:
        print(trouver_index(liste2))
    elif choix ==4:
            print("au revoir")
            choix = 5
            input()
    else:
        print("fais le bon choix")
        input()







