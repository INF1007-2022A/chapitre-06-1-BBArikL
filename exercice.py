#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = []
        for _ in range(0, 10): # TODO: demander les valeurs ici
            values.append(input("Entrez une valeur: "))

    values.sort()
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        words = []
        for _ in range(0, 2):
            words.append(input("Entrez un mot: "))

    for i, word in enumerate(words):
        words[i] = list(word)
        words[i].sort()

    return all(w == words[0] for w in words)


def contains_doubles(items: list) -> bool:
    return len(set(items)) != len(items)


def best_grades(student_grades: dict[str, list[int]]) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    max_moy = 0.
    max_student = ""

    for student, grades in student_grades.items():
        st_moy = sum(grades)/len(grades)
        if st_moy > max_moy:
            max_moy = st_moy
            max_student = student

    return {max_student: max_moy}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    lett_freq = {}
    for char in sentence:
        if char not in lett_freq:
            nb_rep = sentence.count(char)
            # if nb_rep >= 5:  # Les tests ne font pas la vérification de du nombre de répétitions
            lett_freq.update({char: nb_rep})

    # Depuis https://datagy.io/python-sort-a-dictionary-by-values/
    lett_freq = dict(sorted(lett_freq.items(), key=lambda x: x[1], reverse=True))  # noqa: List of tuples given to dict()

    return lett_freq


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    nom_recette = input("Entrez le nom de la recette: ")
    recette = {nom_recette: []}

    ingredient = "..."
    while ingredient != "":
        ingredient = input("Entrez un ingrédient (Laisser vide pour terminer): ")

        if ingredient != "":
            recette[nom_recette].append(ingredient)
    return recette


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    nom_recette = input("Entrez le nom d'une rectte: ")

    if nom_recette in ingredients:
        print(f"Voici les ingrédients de la recette {nom_recette}: {', '.join(ingredients[nom_recette])}")
    else:
        print(f"Recette '{nom_recette}' non trouvée!")


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
