phrase = input("Saisissez une phrase : ")
phrase_liste = phrase.split(" ")
phrase_nombre_de_mot = len(phrase_liste)
print("Il y a {} mots dans votre phrase !".format(phrase_nombre_de_mot))

phrase_renversee = []
est_un_palindrome = 1

for mots in reversed(phrase_liste):
    phrase_renversee.append(mots)

for index, mots in enumerate(phrase_liste):
    if phrase_liste[index] != phrase_renversee[index]:
        est_un_palindrome = 0
        break

if est_un_palindrome == 1:
    print("Vous avez saisis un palindrôme")
else:
    print("Vous avez saisis un mot normal")