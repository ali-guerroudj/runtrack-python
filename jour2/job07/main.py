# Chaîne de caractères initiale
chaine_originale = "abcdefghijklmnopqrstuvwxyz" * 10

# Nombre de lignes de la pyramide
nombre_lignes = 10

# Affichage de la suite pyramidale
index = 0
for ligne in range(1, nombre_lignes + 1):
    # Récupérer les caractères pour cette ligne
    caracteres = chaine_originale[index:index + ligne]
    
    # Afficher la ligne
    print(caracteres.center(nombre_lignes * 2 - 1))
    
    # Mettre à jour l'index pour la prochaine ligne
    index += ligne
