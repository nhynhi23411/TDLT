import math

def tinh_S(x, n):
  s = x
  for k in range(1, n+1):
    tu_so = x ** (2*k+1)
    mau_so = math.factorial(2*k+1)
    s += tu_so / mau_so
  return s

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

ket_qua = tinh_S(x, n)
print("Giá trị của S(x, n) là:", ket_qua)