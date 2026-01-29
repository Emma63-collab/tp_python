class Etudiant:
    nom = ""
    matricule = ""
    notes = ""

    def __init__(self, nom, matricule, notes):
        self.nom = nom
        self.matricule = matricule
        self.notes = notes


    def calculer_moyenne(self):
        somme = 0
        for note in self.notes:
            somme += note

        return round(float(somme/len(self.notes)), 2)
    

    def toString(self):
        print("Nom : {}, matricule : {}".format(self.nom, self.matricule))
        print("Notes : ")
        print(self.notes)
        print("Moyenne : ", self.calculer_moyenne())


a = Etudiant("Abalo", "fjdk-7kfjd", [13, 14, 10, 18])
a.toString()