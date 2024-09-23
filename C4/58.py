xA = float(input("Input xA: "))
yA = float(input("Input yA: "))
xB = float(input("Input xB: "))
yB = float(input("Input yB: "))
import math
AB = abs(math.sqrt((xB-xA)*(xB-xA) + (yB-yA)*(yB-yA)) )
print(AB)