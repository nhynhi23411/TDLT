
def check(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year=None):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            if year is None:
                return "Cần nhập thêm năm để tính số ngày trong tháng 2."
            if check(year):
                return 29
            else:
                return 28
        case _:
            return "Tháng không hợp lệ."

month = int(input("Input month: "))
if month == 2:
    year = int(input("Input year: "))
    print(f"Tháng {month} năm {year} có {days_in_month(month, year)} ngày.")
else:
    print(f"Tháng {month} có {days_in_month(month)} ngày.")
