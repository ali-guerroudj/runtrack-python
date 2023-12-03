def decaler_message(message, decalage):
    resultat = ""
    
    for char in message:
        if char.isalpha():
            # Gérer les majuscules et les minuscules
            offset = ord('A') if char.isupper() else ord('a')
            decalage_modifie = (ord(char) - offset + decalage) % 26
            nouveau_char = chr(offset + decalage_modifie)
            resultat += nouveau_char
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            resultat += char
    
    return resultat

# Exemple d'utilisation
message = input("Entrez le message : ")
decalage = int(input("Entrez le décalage : "))

message_decale = decaler_message(message, decalage)
print("Message décalé :", message_decale)
