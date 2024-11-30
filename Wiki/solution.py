import wikipediaapi
import csv


wiki_wiki = wikipediaapi.Wikipedia('Animal-parse', 'ru')

animals = wiki_wiki.page("Категория:Животные_по_алфавиту")

with open('beasts.csv', 'w') as f:
    animal_names = {}

    for animal in animals.categorymembers:
        animal_names[animal[0]] = animal_names.get(animal[0], 0) + 1
    print(animal_names)
    w = csv.writer(f)
    w.writerows(animal_names.items())
