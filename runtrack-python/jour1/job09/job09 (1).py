article = "ps5"
Prix_unitaire = 300
article_en_stock = 500


print(f"article:{article}.")
print(f"Montant :{Prix_unitaire}€")
print(f"article en stock:{article_en_stock}")

vendeur = int(input("\nBonjours Combien d'article desirer vous ?:"))

article_en_stock -= vendeur


Prix_unitaire *= 1.1

print("\nInformation apres l'achat au sujet de l'inflation:")
print(f"Nom du produit : {article}")
print("Iflation de 10%")
print("\n...")

print(f"prix unitaire apres inflation : {Prix_unitaire: .2f}€")
print(f"Quantité en stock : {article_en_stock} unités")
