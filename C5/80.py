def BMI(height, weight):
    return weight / (height ** 2)

def Classify(bmi):
    match bmi:
        case _ if bmi < 18.5:
            return "Thin"
        case _ if bmi <= 24.9:
            return "Normal"
        case _ if bmi <= 29.9:
            return "Slightly Fat"
        case _ if bmi <= 34.9:
            return "Obesity level 1"
        case _ if bmi <= 39.9:
            return "Obesity level 2"
        case _:
            return "Obesity level 3"

def RiskOfDisease(bmi):
    match bmi:
        case _ if bmi < 18.5:
            return "Low"
        case _ if bmi <= 24.9:
            return "Normal"
        case _ if bmi <= 29.9:
            return "High"
        case _ if bmi <= 34.9:
            return "High"
        case _ if bmi <= 39.9:
            return "Very High"
        case _:
            return "Danger"

print("Enter height (in meters):")
height = float(input())
print("Enter weight (in kilograms):")
weight = float(input())

bmi = BMI(height, weight)
print(f"Your BMI = {bmi:.2f}")
print(f"Classify = {Classify(bmi)}")
print(f"Risk of disease = {RiskOfDisease(bmi)}")
