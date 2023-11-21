Montant_actuelle = 500
Rendement_en_pourcentage = 2


Montant_actuelle = 1200
Rendement_en_pourcentage = 2


Montant_actuelle += 600
Rendement_en_pourcentage += 2


Apres_augmentation = Montant_actuelle * (Rendement_en_pourcentage / 100)


print(f"Gain après augmentation : {Apres_augmentation:.2f} euros")

Montant_actuelle -= 0.10 * Montant_actuelle

Rendement_en_pourcentage -= 1

montant_final = Montant_actuelle * (1 - 0.01 + Rendement_en_pourcentage / 100)

print(f"Montant après retrait : {montant_final:.2f} euros")
print("passez une bonne journée")