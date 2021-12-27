month = int(input("Enter the month number: "))
if month > 12:
    print("Please enter the valid month number !!!")
else:
    year = int(input("Enter the year: "))

    if (month == 2 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0):
        print(f"Number of days present in given {year} is 29")
    elif month == 2:
        print(f"Number of days present in given {year} is 28 ")
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print(f"Number of days present in given {year} is 31")
    else:
        print("Number of days present is 30")
