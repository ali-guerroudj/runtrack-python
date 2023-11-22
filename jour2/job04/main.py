# Demander à l'utilisateur de saisir un entier N
while True:
    try:
        N = int(input("Entrez un entier supérieur à zéro (N) : "))
        if N > 0:
            break
        else:
            print("Veuillez entrer un entier supérieur à zéro.")
    except ValueError:
        print("Veuillez entrer un entier valide.")

# Afficher les tables de multiplication de 1 à N
for i in range(1, N + 1):
    print(f"\nTable de multiplication de {i}:")
    for j in range(1, 11):
        produit = i * j
        print(f"{i} x {j} = {produit}")