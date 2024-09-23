x = int(input("Input x: "))
sum = 0
if x == 0:
    print("Not a perfect number") 
else:
    for i in range(1,x):
        if (x % i == 0):
                sum += i
    if (sum == x):
        print(f"{x} is a perfect number")
    else:
        print("Not a perfect number") 

