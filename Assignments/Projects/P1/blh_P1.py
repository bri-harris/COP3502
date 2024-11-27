import p1_random as p1 #import the module
rng = p1.P1Random() #create a P1Random variable

game_count = 0
win_count = 0
win_percentage = 0
dealer_win_count= 0
tie_count = 0

menu = '''
1. Get another card
2. Hold hand
3. Print statistics
4. Exit
'''

flag = True
while(flag):
    hand_value = 0
    game_count+=1
    print(f"START GAME #{game_count}")
    print()
    my_number = rng.next_int(13)+1
    if my_number == 11:
        print("Your card is a JACK!")
        hand_value+=10
    elif my_number == 12:
        print("Your card is a QUEEN!")
        hand_value+=10
    elif my_number == 13:
        print("Your card is a KING!")
        hand_value+=10
    elif my_number == 1:
        print("Your card is a ACE!")
        hand_value+=1
    else:
        print(f"Your card is a {my_number}!")
        hand_value+= my_number
    print(f"Your hand is: {hand_value}")
    

    while(True):
        print(menu)
        selection = int(input("Choose an option: "))
        print()
# Selection 1
        if selection == 1:
            my_number = rng.next_int(13) + 1
            if my_number == 11:
                print("Your card is a JACK!")
                hand_value+=10
            elif my_number == 12:
                print("Your card is a QUEEN!")
                hand_value+=10
            elif my_number == 13:
                print("Your card is a KING!")
                hand_value+=10
            elif my_number == 1:
                print("Your card is a ACE!")
                hand_value+=1
            else:
                hand_value+= my_number
                print(f"Your card is a {my_number}!")
            print(f"Your hand is: {hand_value}")
            
            if hand_value >21:
                print("You exceeded 21! You lose.")
                print()
                dealer_win_count += 1
                break
            elif hand_value == 21:
                print("BLACKJACK! You win!")
                print()
                win_count += 1
                break
# Selection 2
        elif selection == 2:
            dealer_number = rng.next_int(11) + 16
            print(f"Dealer's hand: {dealer_number}")
            print(f"Your hand is: {hand_value}")
            print()
            if dealer_number > 21 or hand_value > dealer_number:
                print("You win!")
                win_count+= 1
            elif hand_value == dealer_number:
                print("It's a tie! No one wins!")
                tie_count +=1
            else:
                print("Dealer wins!")
                dealer_win_count += 1
            print()
            break
#Selection 3
        elif selection == 3:
            print(f"Number of Player wins: {win_count}")
            print(f"Number of Dealer wins: {dealer_win_count}")
            print(f"Number of tie games: {tie_count}")
            print(f"Total # of games played is: {game_count - 1}")
            if dealer_win_count == 0 or win_count == 0:
                if dealer_win_count > 0:
                    win_percentage = 0
                elif win_count >0:
                    win_percentage = 100
                else:
                    win_percentage = 0
            else:
                win_percentage = (win_count / (game_count - 1))*100
            print(f"Percentage of Player wins: {win_percentage:.1f}%")
# Selection 4
        elif selection == 4:
            flag = False
            break
# Selection Error
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            continue
    

    