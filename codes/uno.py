import random
from collections import Counter

"""Classe qui va créer un objet Carte avec une couleur et une valeur
en respectant un paquet de UNO"""


class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur  # rouge, bleu, vert, jaune, ou joker
        self.valeur = valeur    # 0-9, +2, Passer, Joker, +4

    def __str__(self):
        if self.couleur == "joker":
            return f"{self.valeur}"
        return f"{self.valeur} {self.couleur}"


class Paquet:
    def __init__(self):
        self.cartes = self.creer_paquet()
        random.shuffle(self.cartes)

    def creer_paquet(self):
        couleurs = ["rouge", "jaune", "bleu", "vert"]
        valeurs = [str(i) for i in range(10)] + ["+2", "Passer"]
        cartes = []

        for couleur in couleurs:
            for valeur in valeurs:
                cartes.append(Carte(couleur, valeur))
                cartes.append(Carte(couleur, valeur))  # Deux exemplaires

        # 4 jokers de chaque
        for _ in range(4):
            cartes.append(Carte("joker", "Joker"))
            cartes.append(Carte("joker", "+4"))

        return cartes

    def piocher(self, nb=1):
        cartes_piochees = []
        for _ in range(nb):
            if self.cartes:
                cartes_piochees.append(self.cartes.pop())
        return cartes_piochees


# Initialisation
paquet = Paquet()
joueur = paquet.piocher(7)
bot = paquet.piocher(7)

# Première carte sur la table
carte_en_jeu = paquet.piocher(1)[0]
while carte_en_jeu.couleur == "joker":
    # Évite de commencer avec un joker
    paquet.cartes.insert(0, carte_en_jeu)
    random.shuffle(paquet.cartes)
    carte_en_jeu = paquet.piocher(1)[0]


def cartes_jouables(main, carte_en_jeu):
    """Fonction qui va regarder si les cartes en main sont jouable
    et va retourner les différentes cartes jouable pour le tour"""
    jouables = []
    for carte in main:
        if (
            carte.couleur == carte_en_jeu.couleur
            or carte.valeur == carte_en_jeu.valeur
            or carte.couleur == "joker"
        ):
            jouables.append(carte)
    return jouables


def appliquer_effet(carte, joueur_suivant, paquet):
    """Fonction qui va permettre d'appliquer les effets des cartes
    +2, +4, Joker et passer et affecte des effets selon la carte"""
    effet = carte.valeur

    if effet == "+2":
        print("💥 +2 ! Le joueur suivant pioche 2 cartes et perd son tour.")
        joueur_suivant += paquet.piocher(2)
        return "sauter"

    elif effet == "Passer":
        print("🚫 Tour passé pour le joueur suivant.")
        return "sauter"

    elif effet == "+4":
        print("💥 +4 ! Le joueur suivant pioche 4 cartes et perd son tour.")
        joueur_suivant += paquet.piocher(4)
        return "choix_couleur_sauter"

    elif effet == "Joker":
        print("🎨 Joker ! Vous pouvez changer la couleur.")
        return "choix_couleur"

    return None


def choisir_couleur():
    """Fonction qui permet de choisir la couleur qui doit être jouer
    par le prochain joueur"""
    couleurs = ["rouge", "jaune", "vert", "bleu"]
    print("Choisissez une couleur :")
    for i, c in enumerate(couleurs):
        print(f"{i + 1} - {c}")
    choix = int(input("Votre choix : ")) - 1
    return couleurs[choix]


def couleur_frequente(main):
    """Fonction en place pour le bot qui va permettre
    de choisir une couleur à jouer selon la couleur qui est
    le plus présente dans la main du bot
    """
    couleurs = [c.couleur for c in main if c.couleur != "joker"]
    if couleurs:
        return Counter(couleurs).most_common(1)[0][0]
    return random.choice(["rouge", "jaune", "bleu", "vert"])


def tour_du_bot(bot_main, joueur_main, paquet, carte_en_jeu):
    """Fonction qui permet au bot de lancer son tour"""
    print("\n🤖 Tour du BOT...")

    # Étape 1 : trouver les cartes jouables
    jouables = cartes_jouables(bot_main, carte_en_jeu)

    if jouables:
        carte_choisie = jouables[0]
        bot_main.remove(carte_choisie)
        carte_en_jeu = carte_choisie
        print(f"Le bot joue : {carte_choisie}")

        # Étape 2 : appliquer les effets
        action = appliquer_effet(carte_choisie, joueur_main, paquet)

        if action in ["choix_couleur", "choix_couleur_sauter"]:
            # Le bot choisit la couleur qu'il a le plus en main
            nouvelle_couleur = couleur_frequente(bot_main)
            carte_en_jeu.couleur = nouvelle_couleur
            print(f"Le bot choisit la couleur : {nouvelle_couleur}")

        if action in ["sauter", "choix_couleur_sauter"]:
            return carte_en_jeu, True  # True = le joueur saute son tour

    else:
        print("Le bot ne peut pas jouer. Il pioche une carte.")
        pioche = paquet.piocher(1)
        if pioche:
            bot_main += pioche
            nouvelle = pioche[0]
            if (nouvelle.couleur == carte_en_jeu.couleur
                    or nouvelle.valeur == carte_en_jeu.valeur
                    or nouvelle.couleur == "joker"):
                print(f"Le bot joue la carte piochée : {nouvelle}")
                bot_main.remove(nouvelle)
                carte_en_jeu = nouvelle
                if len(bot_main) == 1:
                    print("🔔 UNO ! Il reste une carte dans la main du bot.")
                if len(bot_main) == 0:
                    print("💀 Le bot a gagné la partie. Vous avez perdu...")
                    exit()

                action = appliquer_effet(nouvelle, joueur_main, paquet)

                if action in ["choix_couleur", "choix_couleur_sauter"]:
                    couleur = couleur_frequente(bot_main)
                    carte_en_jeu.couleur = couleur
                    print(f"Le bot choisit la couleur : {couleur}")

                if action in ["sauter", "choix_couleur_sauter"]:
                    return carte_en_jeu, True

    return carte_en_jeu, False  # False = joueur peut jouer


def boucle_de_jeu():
    """Fonction qui lance le jeu UNO contre un bot"""
    paquet = Paquet()

    joueur = paquet.piocher(7)
    bot = paquet.piocher(7)

    carte_en_jeu = paquet.piocher(1)[0]
    while carte_en_jeu.couleur == "joker":
        paquet.cartes.append(carte_en_jeu)
        random.shuffle(paquet.cartes)
        carte_en_jeu = paquet.piocher(1)[0]

    joueur_saute = False

    while True:
        print("\n" + "-" * 40)
        print(f"🃏 Carte sur la table : {carte_en_jeu}")
        print("-" * 40)

        # Vérifier si le joueur est sauté
        if joueur_saute:
            print("⏭️ Votre tour est sauté.")
            joueur_saute = False
        else:
            print("\n🎮 Votre main :")
            for i, c in enumerate(joueur):
                print(f"{i + 1} - {c}")

            if len(joueur) == 1:
                print("🔔 UNO !")

            # Tour du joueur
            jouables = cartes_jouables(joueur, carte_en_jeu)

            if not jouables:
                print("😕 Aucune carte jouable. Vous piochez.")
                pioche = paquet.piocher(1)
                if pioche:
                    joueur += pioche
            else:
                print("\nCartes jouables :")
                for i, carte in enumerate(jouables):
                    print(f"{i + 1} - {carte}")
                choix = int(input("Choisissez une carte (ex: 1) : ")) - 1
                carte_jouee = jouables[choix]
                joueur.remove(carte_jouee)
                carte_en_jeu = carte_jouee

                if len(joueur) == 0:
                    print("🏆 Vous avez gagné la partie !")
                    break

                action = appliquer_effet(carte_jouee, bot, paquet)
                if action in ["choix_couleur", "choix_couleur_sauter"]:
                    carte_en_jeu.couleur = choisir_couleur()
                if action in ["sauter", "choix_couleur_sauter"]:
                    joueur_saute = False
                    continue  # Le bot est sauté

        # Tour du bot
        carte_en_jeu, saute = tour_du_bot(bot, joueur, paquet, carte_en_jeu)

        if len(bot) == 0:
            print("💀 Le bot a gagné la partie. Vous avez perdu...")
            break

        joueur_saute = saute


if __name__ == "__main__":
    boucle_de_jeu()
