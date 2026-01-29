a = input("Saisir le premier chiffre : ")
b = input("Saisir le second chiffre : ")

try:
    c = int(a)/int(b)
    print("Le résultat de la division est : {}".format(c))
except TypeError:
    print("Veuillez saisir des chiffres")
except ZeroDivisionError:
    print("Le second chiffre doit être différent de zéro")
except ValueError:
    print("Veuillez saisir des chiffres valides")
except Exception as e:
    print(type(e).__name__)