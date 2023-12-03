def distance_toilettes(n, m):
    total_marches = n * 2 # Pour aller et revenir
    total_cm = total_marches * m
    total_m = total_cm / 100 # Conversion de cm en m
    distance_semaine = total_m * 7 # Parcouru par semaine
    return distance_semaine

n = int(input("Entrez le nombre de marches du phare : "))
m = int(input("Entrez la hauteur de chaque marche (en cm) : "))
distance = distance_toilettes(n, m)
print(f"Pour {n} marches de {m} cm, le gardien parcourt {distance:.2f} m par semaine.")