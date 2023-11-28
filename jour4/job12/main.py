def tri_croissant(liste):
    # Vérifier si la liste est vide ou a un seul élément
    if not liste or not liste[1:]:
        return liste

    # Utiliser une boucle while avec IndexError pour parcourir la liste
    swapped = True
    index = 0

    while swapped:
        swapped = False
        index = 0

        try:
            while True:
                if liste[index] > liste[index + 1]:
                    # Échanger les éléments s'ils sont dans le mauvais ordre
                    temp = liste[index]
                    liste[index] = liste[index + 1]
                    liste[index + 1] = temp
                    swapped = True
                index += 1

        except IndexError:
            pass

    return liste

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
resultat = tri_croissant(ma_liste)
print("Liste triée dans l'ordre croissant:", resultat)