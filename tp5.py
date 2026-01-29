notes = []

def calcul_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note

    return round(float(somme/len(liste_notes)), 2)


try:
    with open("notes.txt", "r") as notes_fichier:
        note_lues = notes_fichier.readlines()
        if note_lues:
            for note in note_lues:
                notes.append(float(note))

    print("La moyenne est de {}".format(calcul_moyenne(notes)))

    with open("resultat.txt", "w") as resultat_fichier:
        resultat_fichier.write(str(calcul_moyenne(notes)))


except FileNotFoundError:
    print("Le fichier n'existe pas et sera créé")
    with open("notes.txt", "w") as notes_fichier:
        pass