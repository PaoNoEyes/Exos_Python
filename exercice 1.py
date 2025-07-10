""" codé en UTF-8 """
"""ce programme permet la gestion de la base de donnée de la BA721"""

ba721=[{"prenom":"Erwan", "nom":"Le-Moullec", "age":"25ans", "sexe":"Masculin"},
       {"prenom":"Erwan", "nom":"Guillard", "age":"23ans", "sexe":"Masculin"},
       {"prenom":"Gabin", "nom":"Le-Cam", "age":"27ans", "sexe":"Masculin"},
       {"prenom":"Gabrielle", "nom":"Fonte", "age":"20ans", "sexe":"Féminin"},
       {"prenom":"Clement", "nom":"Fonte", "age":"22ans", "sexe":"Masculin"},
       {"prenom":"Yauwenn", "nom":"Treiber", "age":"28ans", "sexe":"Masculin"}]
choix= 1

def ajouter_un_eleve(liste):
    nom=input("quel est le nom de l'eleve: ")
    prenom=input("quel est le prenom de l'eleve:")
    age=input("quel est l'âge de l'eleve: ")
    sexe = input("quel est son sexe :")
    liste.append({"nom":nom,"prenom":prenom, "age":age, "sexe":sexe})
    return liste

def afficher_les_eleves(liste):
    for i in liste:
        print(i["prenom"],i["nom"], i["age"], i["sexe"])

def supprimer_un_eleve(liste):
    suppression_nom=input("quel est le nom de l'eleve à suprrimer :")
    suppression_prenom=input("quel est le prenom de l'eleve à suprrimer :")
    for i in liste:
            if i["nom"] == suppression_nom and i["prenom"] == suppression_prenom:
                liste.remove(i)
def croissant_par_age(liste):
    liste.sort(key=lambda x:x["age"])
    for i in liste:
        print(i["prenom"], i["nom"], i["age"], i["sexe"])
def trier_par_alphabet(liste):
    liste.sort(key=lambda x:x["nom"])
    for i in liste:
        print(i["prenom"], i["nom"], i["age"], i["sexe"])


while choix in [1,2,3,4,5]:
    choix=int(input("Bienvenue dans la base de donnée des élèves de la BA721, veuillez choisir votre programme :\n "
                "1: ajouter un élève \n 2: afficher la liste des élèves \n "
                "3: trier les élève par ordre croissant d'age\n 4: trier les élèves par ordre alphabétique du nom \n "
                "5: quitter  "))
    if choix==1:
        ajouter_un_eleve(ba721)
        print("bien ajouté")
        input()
    elif choix==2:
        afficher_les_eleves(ba721)
        input()
    elif choix==3:
        croissant_par_age(ba721)
        input()
    elif choix==4:
        trier_par_alphabet(ba721)
        input()
    elif choix==5:
        print("bye bye")
        choix=10
    else:
        print("fais le bon choix connard")
        input()
