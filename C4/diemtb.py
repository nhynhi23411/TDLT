def dtb(t, l, h):
    dtb=(t+l+h)/3
    print("Average score=",dtb)
    print("Rounded score=",round(dtb,2))

t = float(input("Enter math score: "))
l = float(input("Enter chemistry score: "))
h = float(input("Enter physics score: "))

dtb(t, l, h)