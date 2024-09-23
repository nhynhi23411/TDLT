def tinh(N):
    
    S = 1
    for i in range(3, N+1, 3): 
        S *= i
    return S

N = 5
for i in range(N+1, 10):  
    print("====" + str(tinh(i)))