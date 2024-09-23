a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))
import math
if a == 0:
    if b == 0:
        if c == 0:
            print("infinity")
        else:
            print("no solution")
    else:
        print(f"{b}x + {c} =0")
        print(f"x = {-c/b}")
else:
    delta = (b*b) - 4*a*c
    if (delta < 0):
        print("no solution")
    elif (delta == 0): 
        print(f"{a}x^2 + {b}x + {c} =0")
        print(f"x = {-b/2*a}")
    else:
        candelta = math.sqrt(delta)
        x1 = (-b + candelta) / 2*a
        x2 = (-b - candelta) / 2*a
        print(f"{a}x^2 + {b}x + {c} =0")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    


