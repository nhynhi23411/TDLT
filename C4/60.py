n = int(input("Enter a 3-digit integer: "))
a = n % 10
b = a
n = n // 10
a = n % 10
b = b*10 + a
n = n // 10
a = n % 10
b = b*10 + a
print(b)

    