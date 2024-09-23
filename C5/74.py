
ones = {
    0: "",
    1: "một",
    2: "hai",
    3: "ba",
    4: "bốn",
    5: "năm",
    6: "sáu",
    7: "bảy",
    8: "tám",
    9: "chín"
}

tens = {
    1: "mười",
    2: "hai mươi",
    3: "ba mươi",
    4: "bốn mươi",
    5: "năm mươi",
    6: "sáu mươi",
    7: "bảy mươi",
    8: "tám mươi",
    9: "chín mươi"
}

def read_number(n):
    if n < 0 or n > 99:
        return "Số không hợp lệ, vui lòng nhập số từ 0 đến 99"
    
    if n == 0:
        return "không"
    
    if n < 10:
        return ones[n]
    
    ten = n // 10
    one = n % 10

    if one == 0:
        return tens[ten]
    
    if ten == 1 and one == 5:
        return "mười lăm"
    elif ten != 1 and one == 5:
        return f"{tens[ten]} lăm"
    
    if ten == 1:
        return f"mười {ones[one]}"
    
    return f"{tens[ten]} {ones[one]}"

n = int(input("Nhập số (tối đa 2 chữ số): "))
print(read_number(n))
