def calcul_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note

    return round(float(somme/len(liste_notes)), 2)

def saisir_etudiant():
    etudiant = {}
    etudiant["nom"] = input("Saisir votre nom : ")
    etudiant["age"] = input("Saisir votre âge : ")
    etudiant["moyenne"] = input("Saisir moyenne : ")

    print(etudiant)
    return etudiant


etudiants = []
moyennes = []
a = saisir_etudiant()
b = saisir_etudiant()
c = saisir_etudiant()
etudiants.append(a)
etudiants.append(b)
etudiants.append(c)

def afficher_etudiants_admis():
    etudiant_admis = []
    for etudiant in etudiants:
        moyennes.append(float(etudiant["moyenne"]))
        if float(etudiant["moyenne"]) >= 10.0:
            etudiant_admis.append(etudiant)


    for etudiant in etudiant_admis:
        print(etudiant)


print("Liste des étudiants admis : ")
afficher_etudiants_admis()
print("Moyenne générale de la classe : ")
print(calcul_moyenne(moyennes))





