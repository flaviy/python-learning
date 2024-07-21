from os import system

import numbers


def main():
    def clear_console():
        if system('cls') != 0:
            system('clear')

    area_numbers = {}
    areas = {'P': 'Perfumes', 'M': 'Medicine', 'C': 'Cosmetics'}
    for area_letter, area_name in areas.items():
        area_numbers.update({area_letter: numbers.Numbers(area_letter, area_name)})

    while True:
        print('^' * 50)
        print('Select Area: ')
        for area in area_numbers.values():
            print(f'{area.area_letter} :  {area.area_name}')
        print('Q : Quit')

        choice = input('Enter your choice: ')
        if choice not in [area.area_letter for area in area_numbers.values()] and choice != 'Q':
            print('Invalid choice')
            print('Press Enter to continue...')
            input()
            clear_console()
        else:
            if choice == 'Q':
                clear_console()
                continue
            print(f'You selected {areas[choice]}')
            selected_area = area_numbers[choice]
            decorated_function = selected_area.get_current_order_number_decorator(selected_area.get_current_order_number)

            # Call the decorated function
            decorated_function()

            print('Press Enter to continue...')
            input()
            clear_console()


main()
