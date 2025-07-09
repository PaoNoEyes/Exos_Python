#coding UTF8

# Base de données des élèves de la base aérienne 721

eleves = [
    {"prenom": "Erwan", "nom": "Le Moullec", "age": 25, "sexe": "Masculin"},
    {"prenom": "Erwan", "nom": "Guillard", "age": 23, "sexe": "Masculin"},
    {"prenom": "Gabin", "nom": "Le Cam", "age": 27, "sexe": "Masculin"},
    {"prenom": "Clement", "nom": "Fonte", "age": 22, "sexe": "Masculin"},
    {"prenom": "Gabrielle", "nom": "Fonte", "age": 20, "sexe": "Feminin"},
    {"prenom": "Yauwenn", "nom": "Treiber", "age": 28, "sexe": "Masculin"}
]

def afficher_eleves():
    for i in eleves:
        print(f"{i['prenom']} {i['nom']} - {i['age']} ans - {i['sexe']}")

def ajouter_eleve():
    prenom = input("Prenom :")
    nom = input("Nom : ")
    age = input("Age : ")
    sexe = input("Sexe : ")
    eleves.append({"prenom": prenom, "nom": nom, "age": age, "sexe": sexe})

def supprimer_eleve() :
    nom = input("Nom de l'eleve a supprimer :")
    prenom = input("Prenom de l'eleve a supprimer :")
    for i in eleves :
        if i["nom"].lower() == nom.lower() and ["prenom"].lower() == prenom.lower():
            eleves.remove()
            print("Suppression terminée")
            return
    print("eleve non trouvé")

def trier_par_age():
    eleves.sort(key=lambda x: x["age"])
    afficher_eleves()

def trier_par_nom():
    eleves.sort(key=lambda x: x["nom"].lower())
    afficher_eleves()


def menu():
    while True:
        print("=== Menu de gestion des élèves ===")
        print("1. Afficher tous les élèves")
        print("2. Ajouter un élève")
        print("3. Supprimer un élève")
        print("4. Trier par âge")
        print("5. Trier par nom")
        print("6. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            afficher_eleves()
        elif choix == "2":
            ajouter_eleve()
        elif choix == "3":
            supprimer_eleve()
        elif choix == "4":
            trier_par_age()
        elif choix == "5":
            trier_par_nom()
        elif choix == "6":
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.\n")


# Lancement du programme
menu()

