def afficher_tapis_diagonale(n):
    tapis = [["_" for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        tapis[i][i] = "/"
        tapis[i][n-i] = "\\"

    for ligne in tapis:
        print("".join(ligne))

# Test de la fonction avec une taille donnée
taille_tapis = int(input("Entrez la taille du tapis : "))
afficher_tapis_diagonale(taille_tapis)
