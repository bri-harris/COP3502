input_1 = float(input("Enter the price of the item: "))
input_2 = float(input("Enter the sales tax percentage: "))
to_2_decimals = input_1*(1+ input_2*.01)
print(f"Your total is ${to_2_decimals:.2f}")
