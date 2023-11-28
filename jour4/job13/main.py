def supprimer_doublons(liste):
    # Vérifier si la liste est vide ou a un seul élément
    if not liste or not liste[1:]:
        return liste

    liste_sans_doublons = []

    for element in liste:
        # Ajouter l'élément à la nouvelle liste s'il n'est pas déjà présent
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
resultat = supprimer_doublons(ma_liste)
print("Liste sans doublons:", resultat)
