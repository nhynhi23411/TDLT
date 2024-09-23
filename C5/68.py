def check_number(num):
    match num:
        case 1:
            return "Số một"
        case 2:
            return "Số hai"
        case _:
            return "Số khác"

print(check_number(1))  
print(check_number(3))  

def check_type(value):
    match value:
        case int():
            return "Đây là một số nguyên"
        case str():
            return "Đây là một chuỗi"
        case _:
            return "Loại dữ liệu khác"

print(check_type(10))   
print(check_type("hi"))


def check_tuple(data):
    match data:
        case (x, y) if x == y:
            return f"Cặp số {x} và {y} giống nhau"
        case (x, y):
            return f"Cặp số {x} và {y} khác nhau"
        case _:
            return "Không phải là tuple phù hợp"

print(check_tuple((5, 5))) 
print(check_tuple((3, 4)))