n = int(input())
f1 = [[0] * (2 * n) for _ in range(n + 1)]
f2 = [[0] * (2 * n) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, 2 * n):
        f1[i][n - i + 1] = 1
        f1[i][n + i - 1] = 1
        f2[i][n - i + 1] = 1
        f2[i][n + i - 1] = 1
        
        if i > 2 and j > n - i + 1 and j < n + i - 1 and abs(i - j) % 2 == 0:
            f1[i][j] = f1[i - 1][j - 1] + f1[i - 1][j + 1] + 1
            f2[i][j] = f2[i - 1][j - 1] + f2[i - 1][j + 1]


for i in range(n, 0, -1):
    for j in range(1, 2 * n):
        if f1[i][j] != 0:
            print(f1[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

print()

for j in range(1, 2 * n):
    for i in range(1, n + 1):
        if f2[i][j] != 0:
            print(f2[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

print()


for j in range(1, 2 * n):
    for i in range(n, 0, -1):
        if f1[i][j] != 0:
            print(f1[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
