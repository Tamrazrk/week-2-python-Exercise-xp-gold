# Get user input for the month
month = int(input("Enter a month (1 to 12): "))

# Check the season based on the month and display the result
if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month input. Please enter a number between 1 and 12.")
