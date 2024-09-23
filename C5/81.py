def roi(r, c):
    return r/c
def Investment(roi):
    match roi:
        case _ if roi >= 0.75:
            return "Should invest"
        case _:
            return "Don't invest"


print("ROI calculator")
r=int(input("Enter Revenue:"))
c=int(input("Enter cost:"))
roi=roi(r,c)
print("ROI rate =",roi)
print("==>",Investment(roi))