def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            resultat = f"{minutes_restantes} minutes"
        elif heures == 1:
            resultat = f"{heures} heure et {minutes_restantes} minutes"
        else:
            resultat = f"{heures} heures et {minutes_restantes} minutes"

        print(resultat)
    else:
        print("Le paramètre doit être un nombre entier positif")

# Exemples d'appels de la fonction
time_to_text(75)
time_to_text(120)
time_to_text(45)
time_to_text("abc")
time_to_text(-10)