print("=== Programme de division ===")

try:
    a = float(input("Entrez le premier nombre : "))
    b = float(input("Entrez le deuxième nombre : "))

    resultat = a / b
    print("Le résultat de la division est :", resultat)

except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")

except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")

except Exception:
    print("Une erreur inattendue est survenue.")

else:
    print("Division effectuée avec succès.")

finally:
    print("Fin du programme.")
