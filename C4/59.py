import math

def loga_x(a, x):
    return math.log(x) / math.log(a)

a = float(input("Enter value a (a > 0 and a ≠ 1): "))
x = float(input("Enter value x (x > 0): "))

while a <= 0 or a == 1 or x <= 0:
    print("Invalid input value. Please re-enter.")
    a = float(input("Enter value a (a > 0 and a ≠ 1): "))
    x = float(input("Enter value x (x > 0): "))

# Calculate logaₓ
result = loga_x(a, x)
print(f"log_{a}({x}) = {result}")