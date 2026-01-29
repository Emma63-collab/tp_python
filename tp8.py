# TP8 - Algorithmes et complexité

# 1. Implémentation du tri à bulles
liste = [5, 2, 9, 1, 7]

n = len(liste)

for i in range(n):
    for j in range(0, n - i - 1):
        if liste[j] > liste[j + 1]:
            liste[j], liste[j + 1] = liste[j + 1], liste[j]

print("Liste triée avec le tri à bulles :", liste)

# 2. Recherche linéaire
valeur_recherchee = 7
trouve = False

for i in range(len(liste)):
    if liste[i] == valeur_recherchee:
        print(f"Valeur {valeur_recherchee} trouvée à l'indice {i}")
        trouve = True
        break

if not trouve:
    print("Valeur non trouvée")

# 3. Comparaison avec les fonctions Python
liste2 = [5, 2, 9, 1, 7]

liste_triee_python = sorted(liste2)
print("Liste triée avec sorted() :", liste_triee_python)