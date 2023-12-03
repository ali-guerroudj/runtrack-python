def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40: # Echec au test
            notes_arrondies.append(note)
        else: # Réussite au test
            multiple_5 = int(note / 5) * 5
            if note - multiple_5 < 3:
                notes_arrondies.append(multiple_5 + 5)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

notes = [int(input("Entrez la note de l'étudiant : ")) for _ in range(5)]
notes_arrondies = arrondir_notes(notes)
print("Les notes arrondies sont :", notes_arrondies)