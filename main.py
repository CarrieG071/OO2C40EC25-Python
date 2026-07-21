"""
Recipe Box - a tiny CLI recipe manager.

Usage:
    python main.py add "Pancakes" 15 "flour,eggs,milk"
    python main.py list
    python main.py view "Pancakes"
    python main.py delete "Pancakes"
    python main.py search "eggs"
"""

import json
import os
import sys

DATA_FILE = "recipes.json"


def load_recipes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_recipes(recipes):
    f = open(DATA_FILE, "w")
    json.dump(recipes, f, indent=2)


def add_recipe(title, cook_time, ingredients):
    recipes = load_recipes()
    recipe = {
        "title": title,
        "cook_time": int(cook_time),
        "ingredients": ingredients.split(","),
    }
    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Added '{title}'")


def list_recipes():
    recipes = load_recipes()
    for r in recipes:
        print(f"{r['title']} ({r['cook_time']} min)")


def view_recipe(title):
    recipes = load_recipes()
    for r in recipes:
        if r["title"] == title:
            print(f"Title: {r['title']}")
            print(f"Cook time: {r['cook_time']} min")
            print(f"Ingredients: {', '.join(r['ingredients'])}")
            return
    print(f"No recipe found named '{title}'")


def delete_recipe(title):
    recipes = load_recipes()
    recipes = [r for r in recipes if r["title"] != title]
    save_recipes(recipes)
    #Added a check to see if the title was in the recipes, 
    #Prints Deleted if it was
    #Alerts the user that the title was not in the recipe list
    if title in recipe:
        print(f"Deleted '{title}'")
    else:
        print(f"{title} was not found")


def search_recipes(keyword):
    recipes = load_recipes()
    matches = [r for r in recipes if keyword in r["ingredients"]]
    for r in matches:
        print(f"{r['title']} ({r['cook_time']} min)")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    if command == "add":
        add_recipe(sys.argv[2], sys.argv[3], sys.argv[4])
    elif command == "list":
        list_recipes()
    elif command == "view":
        view_recipe(sys.argv[2])
    elif command == "delete":
        delete_recipe(sys.argv[2])
    elif command == "search":
        search_recipes(sys.argv[2])
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
