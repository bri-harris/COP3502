



table_1 = '''
        Per Ticket Cost
     | Before 2pm | After 2pm |
Adult| $ 11.17    | $12.45    |
Child| $ 8.00     | $9.68     |
'''

table_2 = '''
Available movies today:
A)12 Strong: 1)2:30 2)4:40 3)7:50 4)10:50
B)Coco: 1)12:40 2)3:45
C)The Post: 1)12:45 2)3:35 3)7:05 4)9:55
'''
print(table_2)
price = 0
movie_option = input("Movie choice: ")
showtime_selection = int(input("Showtime: "))
flag = True
while(flag):
    if movie_option == 'A':
        if showtime_selection == 1 or showtime_selection == 2 or showtime_selection == 3 or showtime_selection ==4:
            adult_tickets = int(input("Adult tickets: "))
            child_tickets = int(input("Kid tickets: "))
            if adult_tickets + child_tickets >=30:
                print("Invalid option; please restart app...")
                flag = False
            else:
                total = (adult_tickets * 12.45) + (child_tickets * 9.68)
                print(f"Total cost: ${total}")
                flag = False
        else:
            print("Invalid option; please restart app...")
            flag = False            
    elif movie_option == 'B':
        if showtime_selection == 1:
            adult_tickets = int(input("Adult tickets: "))
            child_tickets = int(input("Kid tickets: "))
            if adult_tickets + child_tickets >=30:
                print("Invalid option; please restart app...")
                flag = False
            else:
                total = (adult_tickets * 11.17) + (child_tickets * 8.00)
                print(f"Total cost: ${total}")
                flag = False
        if showtime_selection == 2:
            adult_tickets = int(input("Adult tickets: "))
            child_tickets = int(input("Kid tickets: "))
            if adult_tickets + child_tickets >=30:
                print("Invalid option; please restart app...")
                flag = False
            else:
                total = (adult_tickets * 12.45) + (child_tickets * 9.68)
                print(f"Total cost: ${total}")
                flag = False
        else:
            print("Invalid option; please restart app...")
            flag = False        
    elif movie_option == 'C':
        if showtime_selection == 1:
            adult_tickets = int(input("Adult tickets: "))
            child_tickets = int(input("Kid tickets: "))
            if adult_tickets + child_tickets >=30:
                print("Invalid option; please restart app...")
                flag = False
            else:
                total = (adult_tickets * 11.17) + (child_tickets * 8.00)
                print(f"Total cost: ${total}")
                flag = False   
        if showtime_selection == 2 or showtime_selection == 3 or showtime_selection ==4:
            adult_tickets = int(input("Adult tickets: "))
            child_tickets = int(input("Kid tickets: "))
            if adult_tickets + child_tickets >=30:
                print("Invalid option; please restart app...")
                flag = False
            else:
                total = (adult_tickets * 12.45) + (child_tickets * 9.68)
                print(f"Total cost: ${total}")
                flag = False        
        else:
            print("Invalid option; please restart app...")
            flag = False        
    else:
        print("Invalid option; please restart app...")
        flag = False