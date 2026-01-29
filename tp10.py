# TP10 - Mini-projet de synthèse
# Gestion des étudiants avec POO, fichiers et statistiques

class Etudiant:
    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes

    def calculer_moyenne(self):
        somme = 0
        for note in self.notes:
            somme += note
        return round(somme / len(self.notes), 2)

# Liste vide pour stocker les étudiants
liste_etudiants = []

# Demander combien d'étudiants on veut ajouter
nb_etudiants = int(input("Combien d'étudiants voulez-vous enregistrer ? "))

for i in range(nb_etudiants):
    print(f"\n--- Étudiant {i+1} ---")
    nom = input("Nom de l'étudiant : ")
    matricule = input("Matricule : ")
    
    # On crée une liste vide pour les notes
    notes = []
    nb_notes = int(input("Combien de notes pour cet étudiant ? "))
    
    for j in range(nb_notes):
        note = float(input(f"Note {j+1} : "))
        notes.append(note)
    
    # Créer l'étudiant et l'ajouter à la liste
    etudiant = Etudiant(nom, matricule, notes)
    liste_etudiants.append(etudiant)

print("\nTous les étudiants ont été enregistrés !")

# Écriture des étudiants dans un fichier texte
with open("etudiants.txt", "w") as fichier:
    for etudiant in liste_etudiants:
        # On écrit le nom, le matricule et les notes séparées par des virgules
        notes_str = ",".join(str(note) for note in etudiant.notes)
        fichier.write(f"{etudiant.nom};{etudiant.matricule};{notes_str}\n")

print("Les données ont été enregistrées dans 'etudiants.txt'.")

# Lecture des étudiants depuis le fichier et calcul des statistiques
liste_etudiants_fichier = []

with open("etudiants.txt", "r") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()  # Supprime le \n
        nom, matricule, notes_str = ligne.split(";")
        notes = [float(note) for note in notes_str.split(",")]
        etudiant = Etudiant(nom, matricule, notes)
        liste_etudiants_fichier.append(etudiant)

# Calcul des statistiques
if liste_etudiants_fichier:
    # Moyenne de chaque étudiant
    print("\nMoyenne de chaque étudiant :")
    for etu in liste_etudiants_fichier:
        print(f"{etu.nom} ({etu.matricule}) : {etu.calculer_moyenne()}")

    # Moyenne générale
    moyenne_generale = round(
        sum(etu.calculer_moyenne() for etu in liste_etudiants_fichier) / len(liste_etudiants_fichier), 2
    )
    print(f"\nMoyenne générale de la classe : {moyenne_generale}")

    # Meilleur et plus faible moyenne
    meilleur = max(liste_etudiants_fichier, key=lambda e: e.calculer_moyenne())
    plus_faible = min(liste_etudiants_fichier, key=lambda e: e.calculer_moyenne())
    print(f"Meilleur étudiant : {meilleur.nom} ({meilleur.calculer_moyenne()})")
    print(f"Plus faible étudiant : {plus_faible.nom} ({plus_faible.calculer_moyenne()})")
else:
    print("Aucun étudiant trouvé dans le fichier.")