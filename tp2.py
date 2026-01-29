import random

l = [3, 10.5, 12, 19]

notes = []
for i in range(0, 5):
    notes_tmp = []
    for j in range(0, 5):
        notes_tmp.append(random.randrange(0, 40)/2)
        
    notes.append(notes_tmp)

def calcul_moyenne(liste_notes):
    somme = 0
    for note in liste_notes:
        somme += note

    return round(float(somme/len(liste_notes)), 2)


def mention(moyenne): 
# Barème
# < 10 = ajourné
# 10 - 11 = passable
# 12 - 13 = assez bien
# 14 - 16 = bien
# 17 - 19 = très bien
# 20 = excellent

    mention_obtenue  = "Ajourné"
    
    if moyenne < 10.0:
        mention_obtenue = "Ajourné"
    elif moyenne < 12.0 :
        mention_obtenue = "Passable"
    elif moyenne < 14.0:
        mention_obtenue = "Assez bien"
    elif moyenne < 17.0:
        mention_obtenue = "Bien"
    elif moyenne < 20.0:
        mention_obtenue = "Très bien"
    else:
        mention_obtenue = "Excellent"

    return mention_obtenue


print(notes)
for liste_note in notes:
    moyenne = calcul_moyenne(liste_note)
    
    print(mention(moyenne))
