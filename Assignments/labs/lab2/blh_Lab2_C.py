unit_from = input("Enter the unit you are converting from: ")
unit_to= input("Enter the unit you are converting to: ")
temp = float(input(f"Enter the temperature in {unit_from}: "))


if unit_from[0] =='F':
    if unit_to[0] == 'C':
        # Fahrenheit to Celsius
        print(f"That is {((temp - 32) * (5/9)):.1f} degrees {unit_to}")
    elif unit_to[0] == 'K':
        # Fahrenheit to Kelvin
        temp = ((temp - 32) * (5/9))+273.15
        print(f"That is {temp:.1f} degrees {unit_to}")
    else:
        #Fahrenheit to Fahrenheit
        print(f"That is {temp:.1f} degrees {unit_to}")
elif unit_from[0] =='C':
    if unit_to[0] == 'F':
        # Celsius to Fahrenheit
        print(f"That is {((temp*(9/5))+32):.1f} degrees {unit_to}")
    elif unit_to[0] == 'K':
        # Celsius to Kelvin
        print(f"That is {(temp - 273.15):.1f} degrees {unit_to}")
    else:
        # Celsius to Celsius
        print(f"That is {temp:.1f} degrees {unit_to}")
else:
    if unit_to[0] == 'F':
        # Kelvin to Fahrenheit
        temp =  ((temp - 273.15) * 9/5) + 32
        print(f"That is {temp:.1f} degrees {unit_to}")
    elif unit_to[0] == 'C':
        # Kelvin to Celsius
        print(f"That is {(temp - 273.15):.1f} degrees {unit_to}")
    else:
        print(f"That is {temp:.1f} degrees {unit_to}")
    