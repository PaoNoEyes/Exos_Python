
import requests

url = "https://happyapi.fr/api/devises"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    devises = data["result"]["result"]["devises"]

    for devise in devises:
        code = devise["codeISODevise"]
        taux = devise["taux"]
else:
    print(f"Erreur lors de la requête : {response.status_code}")


def convertisseur_monnaie():
    """fonction qui prendra un dictionnaire
    contenant une monnaie et son taux et permettra de convertir
    une monnaie en une autre"""
    monnaies = {}
    monnaies["dollars"] = {"monnaie": "USD",
                           "taux": 1.1717}
    monnaies["euros"] = {"monnaie": "Euro",
                         "taux": 1.0}
    monnaies["francs pacifique"] = {"monnaie": "XPF",
                                    "taux": 119.5}
    monnaies["yens"] = {"monnaie": "JPY",
                        "taux": 171.8}
    monnaies["livres"] = {"monnaie": "GBP",
                          "taux": 0.86}
    monnaies["wons"] = {"monnaie": "CNY",
                        "taux": 8.410}
    monnaies["francs suisse"] = {"monnaie": "CHF",
                                 "taux": 0.9338}
    monnaies["ancien francs"] = {"monnaie": "FF",
                                 "taux":  6.5595}

    print("Voici les monnaies que vous pouvez convertir : " + ", ".
          join(monnaies.keys()))

    monnaie_base = input("De quelle monnaie partez vous ? ")
    valeur_base = 0
    valeur_user = int(input("Combien voulez vous convertir ? "))
    monnaie_user = input("En quelle monnaie voulez vous "
                         "convertir cette valeur ? ")

    if monnaie_base in monnaies and monnaie_user in monnaies:
        valeur_base = monnaies[monnaie_base]["taux"]
    else:
        print("Cette monnaie n'a pas été ajoutée")

    if monnaie_base == "euros":
        print(f"{valeur_user} {monnaie_base} en {monnaie_user} :\n ",
              valeur_user * monnaies[monnaie_user]["taux"])
    else:
        print(f"{valeur_user} {monnaie_base} en {monnaie_user} :\n ",
              valeur_user/valeur_base)
