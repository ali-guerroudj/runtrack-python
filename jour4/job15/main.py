def tri_a_bulles(arr):
    n = 0
    for _ in arr:
        n += 1

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Échanger les éléments s'ils sont dans le mauvais ordre
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def arrondir_et_trier(liste):
    arr = [0] * 100
    n = 0

    for num in liste:
        # Arrondir le nombre (en supposant toujours 2 décimales)
        arr[n] = int(num * 100 + 0.5) / 100
        n += 1

    tri_a_bulles(arr)

    return arr

# Exemple d'utilisation
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondir_et_trier(ma_liste)
print("Liste arrondie et triée dans l'ordre croissant:", resultat)
