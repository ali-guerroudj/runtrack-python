def my_long_word(longueur, chaine):
    mots_resultats = []
    mot_temp = ""
    is_whitespace = True  # Détermine si le caractère actuel est un espace

    # Parcourir chaque caractère dans la chaîne
    index = 0
    char = chaine[index]

    while char != '\0':
        # Vérifier si le caractère est une lettre
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            mot_temp += char
            is_whitespace = False
        else:
            # Si le caractère est un espace, ajouter le mot_temp à la liste si sa longueur est supérieure à longueur
            mot_length = 0
            for _ in mot_temp:
                mot_length += 1

            if not is_whitespace and mot_temp and mot_temp[-1] != ' ' and mot_length > longueur:
                mots_resultats.append(mot_temp)
            mot_temp = ""
            is_whitespace = True

        index += 1
        char = chaine[index] if index < len(chaine) else '\0'

    # Vérifier le dernier mot après la fin de la chaîne
    mot_length = 0
    for _ in mot_temp:
        mot_length += 1

    if not is_whitespace and mot_temp and mot_temp[-1] != ' ' and mot_length > longueur:
        mots_resultats.append(mot_temp)

    return mots_resultats

# Exemple d'utilisation
chiffre = 3
phrase = "Ceci est un exemple de phrase avec des mots plus longs que 3 caractères."
resultat = my_long_word(chiffre, phrase)
print("Mots plus longs que", chiffre, "caractères:", resultat)

