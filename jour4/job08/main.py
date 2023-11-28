def solve():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    print("Tableau initial :", L)
    
    sum_even = 0
    for i in L:
        if i % 2 == 0:
            sum_even += i
    
    print("Somme des valeurs paires dans la liste :", sum_even)

solve()