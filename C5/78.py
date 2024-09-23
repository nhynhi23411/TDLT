
def find_quarter(month):
    match month:
        case 1 | 2 | 3:
            return "This month is in quarter 1."
        case 4 | 5 | 6:
            return "This month is in quarter 2."
        case 7 | 8 | 9:
            return "This month is in quarter 3."
        case 10 | 11 | 12:
            return "This month is in quarter 4."
        case _:
            return "Invalid month. Please enter from 1 to 12."


def input_month():
    try:
        month = int(input("Enter a month (1-12): "))
        print(find_quarter(month))
    except ValueError:
        print("Invalid input value. Please enter an integer from 1 to 12.")


input_month()