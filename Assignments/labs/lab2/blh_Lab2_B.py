income = float(input("Enter your total income this year: "))
b_1 = 11000
b_2 = 44725
b_3 = 95375
b_4 = 182100
b_5 = 231250
b_6 = 578125




if income < b_1:
    print(f"You owe ${(income * .10):.2f} this year.")
elif income < b_2:
    owed_taxes = b_1*.10 + ((income - b_1) * .12)
    print(f"You owe ${owed_taxes:.2f} this year.")
   
elif income < b_3:
    owed_taxes = (b_1*.10)+ ((b_2 - b_1) * .12) + ((income - b_2) * .22)
    print(f"You owe ${owed_taxes:.2f} this year.")
elif income < b_4:
    owed_taxes = (b_1*.10)+ ((b_2 - b_1) * .12) + ((b_3 - b_2) * .22) +((income - b_3) * .24)
    print(f"You owe ${owed_taxes:.2f} this year.")
elif income < b_5:
    owed_taxes = (b_1*.10)+ ((b_2-b_1) * .12) + ((b_3 - b_2) * .22) + ((b_4 - b_3) * .24) + ((income - b_4) * .32)
    print(f"You owe ${owed_taxes:.2f} this year.")
elif income < b_6:
    owed_taxes = (b_1*.10)+ ((b_2-b_1) * .12) + ((b_3 - b_2) * .22) + ((b_4 - b_3) * .24) + ((b_5 - b_4) * .32) + ((income - b_5) * .35)
    print(f"You owe ${owed_taxes:.2f} this year.")
else:
    owed_taxes = (b_1*.10)+ ((b_2-b_1) * .12) + ((b_3 - b_2) * .22) + ((b_4 - b_3) * .24) + ((b_5 - b_4) * .32) + ((b_6 - b_5) * .35) + ((income - b_6) * .37)
    print(f"You owe ${owed_taxes:.2f} this year.")      
