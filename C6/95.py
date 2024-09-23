def kiemtra(n):
    if n <= 0:
        return 0 
    S = 0
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            S += i
    return S == n

n = int(input('Nhap vao một số n: '))
for i in range(1, n+1):
    if kiemtra(i):
        print(i)