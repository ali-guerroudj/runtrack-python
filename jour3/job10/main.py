def verifie_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Le nombre doit être un chiffre entier et positif"

# Appels de la fonction avec différentes valeurs
resultat1 = verifie_pair_impair(10)
resultat2 = verifie_pair_impair(7)
resultat3 = verifie_pair_impair(0)
resultat4 = verifie_pair_impair(-5)


# Affichage des résultats
print("Résultat 1 :", resultat1)
print("Résultat 2 :", resultat2)
print("Résultat 3 :", resultat3)
print("Résultat 4 :", resultat4)

