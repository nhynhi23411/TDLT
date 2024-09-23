t = int(input("Nhập số tiền: "))
n = int(input("Nhập số năm: "))
r = float(input("Nhập % lãi suất: "))
s = t
r /=100
for i in range (1, n+1):
    for j in range(1, (n*4)+1):
        a = s*r*3
        s = s+a
        
print(s)

