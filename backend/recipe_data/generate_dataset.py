# RAW_recipes dataset source: 
# https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?resource=download&select=RAW_recipes.csv

import os
import csv

current_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_path, 'RAW_recipes.csv')

def remove_tokens(string):
    string = string.replace("'", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    return string

# name, id, minutes, contributer_id, submitted, tags, nutrition, n_steps, steps, description
count = 20
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # drop any recipes with missing data
        if (len(row) != 12):
            continue
        # skip first row that is simply labels
        if (row[0] == "name"):
            continue

        
        ingredients = remove_tokens(row[10])
        print("INGREDIENTS: " + ingredients)

        recipe_name = row[0]
        print("NAME: " + row[0])

        recipe_minutes = row[2]
        print("MINUTES: " + recipe_minutes)

        recipe_tags = remove_tokens(row[5])
        print("TAGS: " + recipe_tags)

        steps = remove_tokens(row[8])
        print("STEPS: " + steps)

        print("\n\n")
        print("--")
        print("\n\n")
        count -= 1
        if count == 0:
            break