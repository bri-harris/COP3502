h = int(input('What would you like the height of the board to be? '))
l = int(input('What would you like the length of the board to be? '))

player_1 = 'x'
player_2 = 'o'


def initialize_board(num_rows,num_cols):
    board = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append('-')
        board.append(row)

    return board


def print_board(board):
    board = board[-1:: -1]
    for i in board:
        for j in range(len(i)):
            print(i[j],end='')
        print()


def insert_chip(board,col,chip_type):
    row_index = 0
    for row in board:
        if row[col] == '-':
            row[col] = chip_type
            return row_index
        row_index += 1


def check_if_winner(board,col,row,chip_type):
    r_count = 0
    c_count = 0

    for i in range(len(board[row]) - 1):
        if board[row][i] == chip_type:
            if board[row][i] == board[row][i + 1]:
                r_count += 1
                if r_count == 3:
                    return True
            else:
                r_count = 0
    for j in range(len(board[row]) - 1):
        if board[j][col] == chip_type:
            if board[j][col] == board[j + 1][col]:
                c_count += 1
                if c_count == 3:
                    return True
            else:
                c_count = 0

    return False


board = initialize_board(h,l)
total_spaces = h * l
total_turns = 0
flag = True

print_board(board)
print()
print('Player 1: x')
print('Player 2: o')
print()

while flag:
    p1_choice = int(input('Player 1: Which column would you like to choose? '))
    row = insert_chip(board, p1_choice, player_1)
    total_turns += 1
    print_board(board)
    print()

    if check_if_winner(board, p1_choice, row, player_1):
        print('Player 1 won the game!')
        flag = False
        break
    elif total_turns == total_spaces:
        print('Draw. Nobody wins.')
        flag = False
        break

    p2_choice = int(input('Player 2: Which column would you like to choose? '))
    row = insert_chip(board, p2_choice, player_2)
    total_turns += 1
    print_board(board)
    print()

    if check_if_winner(board, p2_choice, row, player_2):
        print('Player 2 won the game!')
        flag = False
        break
    elif total_turns == total_spaces:
        print('Draw. Nobody wins.')
        flag = False
        break


