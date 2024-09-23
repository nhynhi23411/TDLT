a = float(input("Input a: "))
b = float(input("Input b: "))
if a == 0:
    if b == 0:
        print("infinity")
    else:
        print("no solution")
else:
    print(f"{a}x + {b} =0")
    print(f"x = {-b/a}")


