def solve():
    L = [8, 24, 48, 2, 16]
    print("Tableau initial :", L)
    
    count = 0
    for i in L:
        if i % 3 == 0:
            count += 1
    
    print("Nombre de multiples de 3 dans la liste :", count)

solve()