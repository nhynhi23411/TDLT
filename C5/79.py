from math import sqrt

def calculate_triangle_area(a, b, c):
    if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Invalid triangle"
    else:
        perimeter = a + b + c
        p = perimeter / 2
        area = sqrt(p * (p - a) * (p - b) * (p - c))
        return area

print("Program to calculate the area of a triangle")
a = float(input("Enter edge a>0: "))
b = float(input("Enter edge b>0: "))
c = float(input("Enter edge c>0: "))


result = calculate_triangle_area(a, b, c)
print("Area =", result)
