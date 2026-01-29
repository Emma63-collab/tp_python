# TP1 - Prise en main et structures de base

# 1. Demander le nom et l'âge de l'utilisateur

nom = input("Entrer votre nom : ")
age = int(input("Entrer votre age: "))

# 2. Vérifier si l'utilisateur est mineur ou majeur
if age >= 18:
    print("Vous êtes majeur(e).")
else :
    print("Vous êtes mineur(e).")

# 3. Afficher tous les nombres pairs entre 1 et 100
print("Nombres pairs entre 1 et 100 :")

for nombre in range(1, 101):
    if nombre % 2 == 0:
        print(nombre)