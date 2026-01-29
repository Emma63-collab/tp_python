# TP9 - Manipulation de données CSV

import csv

departements = {}

# 1. Lecture du fichier CSV
with open("employes.csv", mode="r", newline="", encoding="utf-8") as fichier:
    lecteur = csv.DictReader(fichier)
    
    for ligne in lecteur:
        departement = ligne["departement"]
        salaire = int(ligne["salaire"])

        if departement not in departements:
            departements[departement] = []

        departements[departement].append(salaire)

# 2. Calcul et affichage des moyennes
for departement, salaires in departements.items():
    moyenne = sum(salaires) / len(salaires)
    print(f"{departement} : salaire moyen = {moyenne}")

with open("rapport.txt", mode="w", encoding="utf-8") as rapport:
    for departement, salaires in departements.items():
        moyenne = sum(salaires) / len(salaires)
        rapport.write(f"{departement} : salaire moyen = {moyenne}\n")