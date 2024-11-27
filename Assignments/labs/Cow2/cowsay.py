import sys
from heifer_generator import get_cows
from dragon import Dragon


def list_cows(cows):
    print('Cows available: ', end='')
    for cow in cows:
        print(cow.get_name, end=' ')


def find_cow(name,cows):
    for i in cows:
        if i.get_name == name:
            return i
    return f"Could not find {name} cow!"


if __name__ == '__main__':
    cows = get_cows()

    if sys.argv[1] == '-l':
        list_cows(cows)
    elif sys.argv[1] == '-n':
        cow = find_cow(sys.argv[2],cows)
        if isinstance(cow,str):
            print(cow)
        else:
            print(' '.join(sys.argv[3:]))
            print(cow.get_image)
            if isinstance(cow, Dragon):
                if cow.can_breath_fire:
                    print('This dragon can breathe fire.')
                else:
                    print('This dragon cannot breathe fire.')

    else:
        cow = find_cow('heifer',cows)
        print(' '.join(sys.argv[1:]))
        print(cow.get_image)




