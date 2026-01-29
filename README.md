# TP_PYTHON – Portfolio des Travaux Pratiques

Ce dépôt contient l'ensemble des travaux pratiques réalisés dans le cadre du module Python, du TP1 au TP10. Chaque TP est conçu pour développer vos compétences en programmation, algorithmique, gestion de fichiers, POO et traitement de données.

---

## Contenu du dépôt

- `tp1.py` – TP1 : Prise en main et structures de base  
- `tp2.py` – TP2 : Fonctions et modularité  
- `tp3.py` – TP3 : Listes, tuples et dictionnaires  
- `tp4.py` – TP4 : Manipulation de chaînes de caractères  
- `tp5.py` – TP5 : Fichiers (lecture et écriture)  
- `tp6.py` – TP6 : Gestion des exceptions  
- `tp7.py` – TP7 : Programmation Orientée Objet (POO)  
- `tp8.py` – TP8 : Algorithmes et complexité  
- `tp9.py` – TP9 : Manipulation de données CSV  
- `tp10.py` – TP10 : Mini-projet de synthèse (Gestion des étudiants avec POO, fichiers et statistiques)

---

## Description des TP

### TP1 – Prise en main et structures de base
**Contexte réel :** Création d’un premier script utilisé par un service de scolarité  
**Objectifs :** Variables, conditions, boucles  
**Travail demandé :**
1. Demander le nom et l’âge de l’utilisateur  
2. Vérifier si l’utilisateur est majeur ou mineur  
3. Afficher tous les nombres pairs entre 1 et 100  
**Compétences visées :** `input()`, `print()`, `if/else`, boucles `for`

---

### TP2 – Fonctions et modularité
**Contexte réel :** Automatisation du calcul des moyennes d’une classe  
**Objectifs :** Définir et utiliser des fonctions  
**Travail demandé :**
1. Créer une fonction `calcul_moyenne(liste_notes)`  
2. Créer une fonction `mention(moyenne)` qui retourne : Ajourné, Passable, Assez bien, Bien, Très bien  
3. Tester avec plusieurs listes de notes  
**Compétences visées :** `def`, paramètres et valeurs de retour

---

### TP3 – Listes, tuples et dictionnaires
**Contexte réel :** Gestion simplifiée des résultats académiques  
**Objectifs :** Structures de données  
**Travail demandé :**
1. Stocker une liste d’étudiants (nom, âge, moyenne)  
2. Afficher les étudiants admis (moyenne ≥ 10)  
3. Calculer la moyenne générale de la classe  
**Compétences visées :** listes, dictionnaires, parcours de collections

---

### TP4 – Manipulation de chaînes de caractères
**Contexte réel :** Analyse de commentaires saisis par des utilisateurs  
**Objectifs :** Traitement de texte  
**Travail demandé :**
1. Demander une phrase à l’utilisateur  
2. Compter le nombre de mots  
3. Trouver le mot le plus long  
4. Vérifier si la phrase est un palindrome  
**Compétences visées :** méthodes sur les chaînes, découpage et analyse

---

### TP5 – Fichiers (lecture et écriture)
**Contexte réel :** Sauvegarde et exploitation de données scolaires  
**Objectifs :** Persistance des données  
**Travail demandé :**
1. Créer un fichier `notes.txt` contenant des notes  
2. Lire le fichier et calculer la moyenne  
3. Écrire le résultat dans un fichier `resultat.txt`  
**Compétences visées :** `open()`, modes `r`, `w`, `a`

---

### TP6 – Gestion des exceptions
**Contexte réel :** Sécurisation d’une application utilisée par des non-informaticiens  
**Objectifs :** Robustesse des programmes  
**Travail demandé :**
1. Créer un programme de division  
2. Gérer les erreurs de type division par zéro, saisie invalide  
3. Afficher des messages personnalisés  
**Compétences visées :** `try / except / finally`

---

### TP7 – Programmation Orientée Objet (POO)
**Contexte réel :** Modélisation d’un système de gestion des étudiants  
**Objectifs :** Classes et objets  
**Travail demandé :**
1. Créer une classe `Etudiant`  
2. Attributs : nom, matricule, notes  
3. Méthodes : calculer la moyenne, afficher les informations  
**Compétences visées :** `class`, `__init__`, méthodes

---

### TP8 – Algorithmes et complexité
**Contexte réel :** Optimisation d’un programme utilisé à grande échelle  
**Objectifs :** Raisonnement algorithmique  
**Travail demandé :**
1. Implémenter le tri à bulles  
2. Implémenter la recherche linéaire  
3. Comparer le temps d’exécution avec les fonctions Python  
**Compétences visées :** algorithmes, complexité

---

### TP9 – Manipulation de données CSV
**Contexte réel :** Analyse de données RH d’une entreprise  
**Objectifs :** Traitement de données  
**Travail demandé :**
1. Lire un fichier CSV d’employés  
2. Calculer le salaire moyen par département  
3. Générer un rapport textuel  
**Compétences visées :** module `csv`, structuration des données

---

### TP10 – Mini-projet de synthèse
**Contexte réel :** Développement d’une application utile à une organisation réelle  
**Objectifs :** Intégration des acquis  
**Travail demandé :**
1. Gérer des étudiants avec POO  
2. Enregistrer les données dans un fichier  
3. Afficher des statistiques (moyenne générale, meilleur et plus faible étudiant)  
4. Livrer le code source et le rapport explicatif  
**Compétences visées :** POO, gestion des fichiers, calculs statistiques, saisie interactive

---

## Instructions pour exécuter les TP

Chaque TP est autonome et peut être exécuté individuellement.  
Exemple pour TP10 :  

```bash
python tp10.py