n = int(input("Input n: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()


for i in range(1, n+1):
    for j in range(1, n+1):
        if j >= n - i + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

for i in range(1, 2*n):
    for j in range(1, 2*n):
        if i == j or (i < n and j == 1) or (i > n and j == 2*n-1) or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
