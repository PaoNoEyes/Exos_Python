liste = [596, 321, 293, 265, 19, 918, 239, 684, 772, 441, 777, 548, 662, 968, 90, 22, 417, 312, 206, 540, 434, 887, 771,]


def trier_liste_decroissante(liste):
    """
    Trie une liste d'entiers par ordre décroissant.

    Paramètres :
        liste (list) : Liste de nombres entiers.

    Retour :
        list : Liste triée en ordre décroissant.

    Excepte :
        ValueError : Si la liste passée est vide.
    """

    # Vérification que la liste n'est pas vide
    if not liste:
        raise ValueError("Erreur : la liste fournie est vide.")

    # Tri de la liste par ordre décroissant
    liste_triee = sorted(liste, reverse=True)

    return liste_triee


# Boucle de tri
if __name__ == "__main__":
    try:
        chiffres = liste
        resultat = trier_liste_decroissante(chiffres)
        print("Liste triée par ordre décroissant :", resultat)
    except ValueError as erreur:
        print(erreur)
