def solve():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    print("Tableau initial :", L)

    product = 1
    for i in L:
        if 25 <= i <= 90:
            product *= i
    print("Le produit de toutes les valeurs de la liste comprises dans l'intervalle [25, 90] est :", product)

solve()