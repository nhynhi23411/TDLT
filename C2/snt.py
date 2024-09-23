x = int(input("Input x: "))
count = 0
for i in range(1,x+1):
    if (x % i == 0):
            count += 1
if (count == 2):
    print(f"{x} is a prime number")
else:
    print("Not a prime number") 

