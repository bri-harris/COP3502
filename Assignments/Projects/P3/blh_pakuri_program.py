from blh_pakuri import *
from blh_pakudex import *

welcome = 'Welcome to the Pakudex: Tracker Extraordinaire!'
capacity_msg = 'Enter max capacity of the Pakudex: '
menu = '''
Pakudex Main Menu
-----------------
1. List Pakuri
2. Show Pakuri
3. Add Pakuri
4. Evolve Pakuri
5. Sort Pakuri
6. Exit
'''
q = 'What would you like to do? '


def begin():
    print(welcome)
    while True:
        try:
            cap = int(input(capacity_msg))
            print(f"The Pakudex can hold {cap} species of Pakuri.")
            return Pakudex(cap)
        except ValueError as e:
            print("Please enter a valid size.")


def prompt_menu():
    print(menu)
    try:
        selection = int(input(q))
    except ValueError as e:
        selection = 'Unrecognized menu selection!'
    return selection


def list_pakuri(dex):
    if (dex.get_size == 0):
        return 'No Pakuri in Pakudex yet!'
    else:
        r = 'Pakuri In Pakudex:\n'
        l = dex.get_species_array
        for i in range(len(l)):
            r += f'{i + 1}. {l[i]}\n'
        return r


def show_species(request, dex):
    try:
        species_stats = dex.get_stats(request)
        r = f'Species: {request}'
        a = f'Attack: {species_stats[0]}'
        d = f'Defense: {species_stats[1]}'
        s = f'Speed: {species_stats[2]}'
    except TypeError as e:
        # print(e)
        return 'Error: No such Pakuri!'
    return '\n' + r + '\n' + a + '\n' + d + '\n' + s


def add_species(species, dex):
    status = dex.add_pakuri(species)
    if status:
        print(f'Pakuri species {species} successfully added!')
    else:
        print('Error: Pakudex already contains this species!')


def evolve(species, dex):
    bool = dex.evolve_species(species)
    if bool:
        print(f'{species} has evolved!')
    else:
        print('Error: No such Pakuri!')


if __name__ == '__main__':
    pakudex = begin()
    while True:
        choice = prompt_menu()
        if choice == 1:
            print(list_pakuri(pakudex))
        elif choice == 2:
            request = input('Enter the name of the species to display: ')
            print(show_species(request,pakudex))
        elif choice == 3:
            if pakudex.get_capacity == pakudex.get_size:
                print('Error: Pakudex is full!')
            else:
                request = input('Enter the name of the species to add: ')
                add_species(request,pakudex)
        elif choice == 4:
            request = input('Enter the name of the species to evolve: ')
            evolve(request, pakudex)
        elif choice == 5:
            pakudex.sort_pakuri()
            print('Pakuri have been sorted!')
        elif choice == 6:
            print('Thanks for using Pakudex! Bye!')
            break
        else:
            print('Unrecognized menu selection!')






# ['Pikabu', 'Charasaurus', 'PsyGoose']