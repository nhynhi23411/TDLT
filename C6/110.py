import math
n = int(input("Nhập số người: "))
x = int(input("Nhập số người khỏi bệnh: "))
m = n - x
ans = (m * math.factorial(n-1)) / math.factorial(n)
print(f"Xác xuất cần tìm là {ans}")