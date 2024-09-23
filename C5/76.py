def check(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def next_day(day, month, year):
    days_in_month = [31, 29 if check(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day += 1
    if day > days_in_month[month - 1]:
        day = 1
        month += 1 
    
    if month > 12:
        month = 1
        year += 1 
    
    return day, month, year

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

next_day_result = next_day(day, month, year)

print(f"Next day: {next_day_result[0]}/{next_day_result[1]}/{next_day_result[2]}")
