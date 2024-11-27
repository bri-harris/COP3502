year_1 = int(input("Enter the year for date 1: "))
month_1 = int(input("Enter the month for date 1: "))
day_1 = int(input("Enter the day for date 1: "))

year_2 = int(input("Enter the year for date 2: "))
month_2 = int(input("Enter the month for date 2: "))
day_2 = int(input("Enter the day for date 2: "))

yr_days_dif = (year_2 - year_1) * 360
month_diff = (month_2 -month_1) * 30
days_diff = (day_2 - day_1)
calc = abs(yr_days_dif + month_diff + days_diff)


print(f"The difference between {month_1}/{day_1}/{year_1} and {month_2}/{day_2}/{year_2} is {calc} days!")


