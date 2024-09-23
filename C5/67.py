i = int(input("Input i: "))
j = int(input("Input j: "))
k = int(input("Input k: "))
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k

print("i =", i, ", j =", j, ", k =", k)
