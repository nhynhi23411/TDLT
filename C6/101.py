n = 4

# Hình 1
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i == n:
            print("*", end=" ")
        elif i < n and n <= j <= n + i - 1:
            print("*", end=" ")
        elif i > n and j <= n and j <= 2 * n - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Hình 2
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i == n or (i < n and j == n) or (i > n and j == 1):
            print("*", end=" ")
        elif i < n and j == n + i - 1:
            print("*", end=" ")
        elif i > n and j == 2 * n - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Hình 3
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i + j == 2 * n or (j > n and j <= 2 * n - i) or (j < n and j >= 2 * n - i + 1) or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()

# Hình 4
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if i + j == 2 * n or (j > n and i == 1) or (j < n and i == 2 * n - 1) or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
