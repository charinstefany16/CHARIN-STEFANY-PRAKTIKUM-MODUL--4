#CHARIN STEFANY
#065002400015


while True:
    month = int(input("Enter the month (1-12): "))
    
    if month == -1:
        print("Program stopped.")
    else:
        year = int(input("Please enter the year (e.g., 2023): "))
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("There are 31 days in the month")
    elif month in [4, 6, 9, 11]:
        print("There are 30 days in the month")

#TAHUN KABISAT
    elif month == 2:
        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
            print("There are 29 days in the month")
else:
    print("There are 28 days in the month")