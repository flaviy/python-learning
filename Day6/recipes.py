from pathlib import Path
from os import system


def get_full_path_to_recipes():
    base = Path.home()
    return Path(base, 'PycharmProjects', 'pythonProject', 'Day6', 'Recipes')


def clear_console():
    if system('cls') != 0:  # If 'cls' command fails (non-zero status)
        system('clear')  #


def select_category():
    print('You have following categories: ')
    categories = [category.name for category in Path(get_full_path_to_recipes()).iterdir() if category.is_dir()]
    print('\n'.join([f'{index + 1}. {category}' for index, category in enumerate(categories)]))
    selected_category = input('Enter index the category: ')
    if not selected_category.isdigit() or int(selected_category) > len(categories):
        print('Invalid category index')
        return select_category()
    print(f'You selected {categories[int(selected_category) - 1]}')
    print('*' * 50)
    return categories[int(selected_category) - 1]

def select_recipe(category):
    print(f'You have following recipes in {category}: ')
    recipies = [recipe.name for recipe in Path(get_full_path_to_recipes() / category).iterdir() if recipe.is_file()]
    print('\n'.join([f'{index + 1}. {Path(recipe).stem}' for index, recipe in enumerate(recipies)]))
    selected_recipe = input('Enter index the recipe: ')
    if not selected_recipe.isdigit() or int(selected_recipe) > len(recipies):
        print('Invalid recipe index')
        return select_recipe(category)
    print(f'You selected {recipies[int(selected_recipe) - 1]}')
    print('*' * 50)
    return recipies[int(selected_recipe) - 1]


def create_recipe(category):
    recipe_name = input('Enter the name of the recipe: ')
    recipe_content = input('Enter the content of the recipe: ')
    path = Path(get_full_path_to_recipes() / category / Path(recipe_name + '.txt'))
    if path.exists():
        overwrite = input('The recipe already exists. Do you want to overwrite it? (y/n): ')
        if overwrite.lower() != 'y':
            print('The recipe is not created')
            print('Press Enter to continue...')
            input()
            clear_console()
            return
    Path(get_full_path_to_recipes() / category / Path(recipe_name + '.txt')).write_text(recipe_content)
    print('The recipe is created')
    print('Press Enter to continue...')
    input()
    clear_console()


def create_category():
    category_name = input('Enter the name of the category: ')
    if category_name and not category_name.isspace():
        path = Path(get_full_path_to_recipes() / category_name)
        if path.exists():
            print('The category already exists')
            return
        path.mkdir()
        print('The category is created')
        input('Press Enter to continue...')
        clear_console()
    else:
        print('The category name is invalid')
        create_category()


def delete_recipe(category, recipe):
    path = Path(get_full_path_to_recipes() / category / recipe)
    delete_recipe = input('Are you sure you want to delete the recipe? (y/n): ')
    if delete_recipe.lower() == 'y':
        path.unlink()
        print('The recipe is deleted')
        print('Press Enter to continue...')
        input()
        clear_console()
    else:
        print('The recipe is not deleted')
        print('Press Enter to continue...')
        input()
        clear_console()


def delete_category(category):
    path = Path(get_full_path_to_recipes() / category)
    delete_category = input('Are you sure you want to delete the category? (y/n): ')
    if delete_category.lower() == 'y':
        for recipe in path.iterdir():
            recipe.unlink()
        path.rmdir()
        print('The category is deleted')
        print('Press Enter to continue...')
        input()
        clear_console()
    else:
        print('The category is not deleted')
        print('Press Enter to continue...')
        input()
        clear_console()


print('Hello, welcome to the Recipe App!')

print(f'The path to the recipes tree is {get_full_path_to_recipes()}')


while True:
    print('^' * 50)
    print('Main menu: ')
    print('1. View recipy')
    print('2. Create a recipe')
    print('3. Create new recipies category')
    print('4. Delete a recipe')
    print('5. Delete recipies category')
    print('6. Exit')

    choice = input('Enter your choice: ')
    match choice:
        case '1':
            category = select_category()
            recipe = select_recipe(category)
            print(f'The recipe is: {Path(get_full_path_to_recipes() / category / recipe).read_text()}')
            print('Press Enter to continue...')
            input()
            clear_console()
        case '2':
            category = select_category()
            create_recipe(category)
        case '3':
            create_category()
        case '4':
            category = select_category()
            recipe = select_recipe(category)
            delete_recipe(category, recipe)

        case '5':
            category = select_category()
            delete_category(category)
        case '6':
            print('Exit')
            clear_console()
            break
        case _:
            print('Invalid choice')
