def affiche_type_developpeur(langage):
    if langage == "JavaScript":
        print("Tu es un développeur web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

# Exemples d'appels de la fonction
affiche_type_developpeur("JavaScript")
affiche_type_developpeur("python")
affiche_type_developpeur("java")
affiche_type_developpeur("reactjs")