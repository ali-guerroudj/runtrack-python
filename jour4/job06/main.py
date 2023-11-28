def solve():
    L = [1, 2, 3, 4, 5]
    print("Tableau initial :", L)
    
    update_L(L)
    print("Tableau après mise à jour :", L)

def update_L(L):
  L[0],L[4] = L[4],L[0]

solve()


