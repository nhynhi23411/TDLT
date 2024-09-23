import math

def dt(r):
    a=r**2
    return a
def cv(r):
    b=2*math.pi*r
    return b
r = float(input("Input r: "))
print(f"Acreage:  {dt(r)}")
print(f"Perimeter:  {cv(r)}")
