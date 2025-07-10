def salut():
    print("B0nj0ur")
    print("Je su1s Tr3ib0ps le f4rf4det m4lic1eux...")
    print("J'ai r00té votre pr0gr4mme pyth0n gr4ce a un3 inject10n sql en tr4vers4l p4th sur l4 bdd.")
    print("j'4i gl1ssé qu3lqu3s 3rr3ur d4ns l3 c0d3, à v0us de d3bugguer, b0nn3 ch4nc3 !")
salut()
"""
Ce programme est crée dans le but de gérer une bibliothèque musicale.
il permet d'ajouter ou supprimer des titres,
de rechercher dans la bibliothèque


/!\ CE CODE NE FONCTIONNE PAS
Je ne sais pas ce que j'ai mal fait, mais il semblerait qu'un farfadet malicieux a bidouillé mon code et l'a modifié...
J'ai besoin de votre aide, jeunes aventurier du python !

"""



bibliothèque_musicale = [                                                               #La bibliothèque ne s'initialise pas...
  {
    "The Beatles": [
      "Come Together",
      "Something",
      "Maxwell's Silver Hammer",
      "Oh! Darling",
      "Octopus's Garden",
      "I Want You (She's So Heavy)",
      "Here Comes the Sun",
      "Because"
    ]
  },
  {
    "Nirvana": [
      "Smells Like Teen Spirit",
      "In Bloom",
      "Come as You Are",
      "Breed",
      "Lithium",
      "Polly",
      "Territorial Pissings",
      "Drain You"
    ]
  },
  {
    "Pink Floyd": [
      "Speak to Me",
      "Breathe",
      "Time",
      "Money",
      "Us and Them",
      "Any Colour You Like",
      "Brain Damage",
      "Eclipse"
    ]
  },
  {
    "Queen": [
      "Death on Two Legs",
      "Lazing on a Sunday Afternoon",
      "I'm in Love with My Car",
      "You're My Best Friend",
      "'39",
      "Bohemian Rhapsody",
      "God Save the Queen"
    ]
  },
  {
    "Led Zeppelin": [
      "Black Dog",
      "Rock and Roll",
      "The Battle of Evermore",
      "Stairway to Heaven",
      "Misty Mountain Hop",
      "Four Sticks",
      "Going to California",
      "When the Levee Breaks"
    ]
  },
  {
    "The Rolling Stones": [
      "Gimme Shelter",
      "Love in Vain",
      "Country Honk",
      "Live with Me",
      "Let It Bleed",
      "Midnight Rambler",
      "You Can't Always Get What You Want"
    ]
  },
  {
    "Radiohead": [
      "Airbag",
      "Paranoid Android",
      "Subterranean Homesick Alien",
      "Exit Music (For a Film)",
      "Let Down",
      "Karma Police",
      "No Surprises",
      "Lucky"
    ]
  },
  {
    "The Strokes": [
      "Is This It",
      "The Modern Age",
      "Soma",
      "Barely Legal",
      "Someday",
      "Last Nite",
      "Hard to Explain",
      "Take It or Leave It"
    
  },
  {
    "Foo Fighters": [
      "All My Life",
      "Times Like These",
      "Disenchanted Lullaby",
      "Tired of You",
      "Halo",
      "Low",
      "Come Back"
    ]
  },
  {
    "Red Hot Chili Peppers": [
      "Around the World",
      "Parallel Universe",
      "Scar Tissue",
      "Otherside",
      "Californication",
      "Porcelain",
      "Road Trippin'"
    ]
  }
]

def ajouter_artiste(nom_du_groupe,liste_tracks):                                        #Cette fonction semble fonctionner
    """
    Cette fonction permet d'ajouter un artiste et ses tracks à la bibliothèque

    Entrée :    str(nom_du_groupe -> contient le nom du group)
                list(liste_tracks -> contient des nom de morceau en str)

    Sortie :    int(0 -> signifie que la fonction s'est terminée correctement)
    """
    bibliothèque_musicale.append({nom_du_groupe : liste_tracks})
    return 0

def supprimer_artiste(nom_du_groupe):
    """
    Cette fonction permet de supprimer un artiste et ses tracks de la bibliothèque

    Entrée :    str(nom_du_groupe -> contient le nom du group)

    Sortie :    int(0 -> signifie que la fonction s'est terminée correctement)
    """

    bibliothèque_musicale.remove(nom_du_groupe)                                         #la fonction ne reconnait pas les groupes


def rechercher_track(track):                                                            #la fonction ne gère pas les majuscules/minuscules...
    """
    Cette fonction permet de rechercher un morceau dans la bibliothèque

    Entrée :    str(track -> contient le nom du morceau)

    Sortie :    int(0 -> signifie que la fonction s'est terminée correctement)
    """
    trouvé = False
    artiste = ''
    for i in bibliothèque_musicale:
        if track in i.values():
            trouvé = True
            artiste = i.keys()
    if trouvé == False:
        print("Ce morceau n'est pas dans la bibiothèque")
    else : 
        print("Ce morceau de",artiste,"est dans la bibliothèque")
    return 0

def afficher_bibli():
    """
    Cette fonction permet d'afficher la bibliothèque

    Entrée :    Aucune

    Sortie :    int(0 -> signifie que la fonction s'est terminée correctement)
    """
    for i in bibliothèque_musicale :
        print("vous avez",len(i[i.keys(0)]),"morceau du groupe",i.keys(0),"\n")         #il semblerait que le parcours ne fonctionne pas correctement

        for i in i.keys(0):
            print(i.keys(0)[i])
    
    return 0




ajouter_artiste("Muse",["supermassive black hole", "ignore world"])                     #test fonc ajouter_artiste
supprimer_artiste("Muse")                                                               #test fonc supprimer_artiste
rechercher_track("californication")                                                     #test fonc rechercher_track
afficher_bibli()                                                                        #test fonc afficher_bibli

