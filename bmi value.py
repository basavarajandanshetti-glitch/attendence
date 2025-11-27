import sys

if len(sys.argv) == 3:
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided weight and height")
else:
    
    weight = 70.0
    height = 1.75
    print("Default weight and height used")

bmi = weight / (height * height)

print("Weight (kg):", weight)
print("Height (m):", height)
print("BMI:", bmi)