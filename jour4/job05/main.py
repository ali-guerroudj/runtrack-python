def update_L(L):
    L[3] = L[2] + L[4]

def solve():
    L = [1, 2, 3, 4, 5]
    print("Tableau initial :", L)

    print("Deuxième valeur de la liste :", L[1])
    
    update_L(L)
    print("Tableau après mise à jour :", L)
    
   
    print("Dernière valeur de la liste :", L[4])

solve()