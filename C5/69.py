def check(year):
    if (year % 4 ==0 and year % 100 != 0) or year % 400 == 0:
        print("Year ", year, " is a leap year")
    else:
        print("Year ", year, " is not a leap year")
print("Leap year test program")
year=int(input("Please enter a year:"))
check(year)

