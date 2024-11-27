import math

menu = '''
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
'''

selection_display = 'Enter Menu Selection: '
skip_menu_selection = False
num = 0
avg = 0
total_result = 0.0
op_result = 0
begin = True

display_stats = f'''
Sum of calculations: {total_result}
Number of calculations: {num}
Average of calculations: {avg:.2f}

'''

while(True):
    if begin == True:
        print(f"Current Result: 0.0")
        print(menu)
        begin = False
    elif skip_menu_selection == False:
        op_result == round(float(op_result),2)
        print(f"Current Result: {op_result}")
        print(menu)
        
        
    selection = int(input(selection_display))
        # operand_1 = float(input(f"Enter first operand: "))
        # operand_2 = float(input("Enter second operand: "))
        # if  operand_1 == "RESULT":
        #     operand_1 = float(op_result )
        # if operand_2 == "RESULT":
        #     operand_2 = float(op_result )
    
    if selection == 0:
        print("Thanks for using this calculator. Goodbye!")
        break
    elif selection == 1:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )        
        else:
            operand_2 = float(operand_2)
        op_result = operand_1 + operand_2
        total_result += op_result
        num += 1
    elif selection == 2:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )
        else:
            operand_2 = float(operand_2)
        op_result = operand_1 - operand_2
        total_result += op_result
        num +=1
    elif selection == 3:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )
        else:
            operand_2 = float(operand_2)
        op_result = operand_1 * operand_2
        total_result += op_result
        num +=1
    elif selection == 4:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )
        else:
            operand_2 = float(operand_2)
        if int(operand_2) == 0:
            print("Error: invalid input!")
            continue
        else:
            op_result = operand_1 / operand_2
            total_result += op_result 
            num +=1
    elif selection == 5:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )
        else:
            operand_2 = float(operand_2)
        if operand_1==1 or operand_1 == 0:
            print("Error: invalid input!")
        else:
            op_result = operand_1 ** operand_2
            total_result += op_result
            num += 1               
    elif selection == 6:
        operand_1 = input(f"Enter first operand: ")
        if  operand_1 == "RESULT":
            operand_1 = float(op_result )
        else:
            operand_1 = float(operand_1)

        operand_2 = input("Enter second operand: ")
        if operand_2 == "RESULT":
            operand_2 = float(op_result )
        else:
            operand_2 = float(operand_2)
        if operand_1 <= 1:
            print("Error: invalid input!")
        else:   
            op_result = math.log(operand_2,operand_1)
            total_result += op_result 
            num +=1
    elif selection == 7:
        if num == 0:
            print(f"Error: No calculations yet to average!\n")
        else:
            avg = total_result / num
            display_stats = f'''Sum of calculations: {total_result}
Number of calculations: {num}
Average of calculations: {avg:.2f}
'''
            print(display_stats)
        skip_menu_selection = True
        continue
    else:
        print(f"Error: Invalid selection!\n")
        skip_menu_selection = True
        continue
    skip_menu_selection = False
        
