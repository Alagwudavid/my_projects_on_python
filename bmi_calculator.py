import  math
print(f"{'#'*3}BMI WEIGHT CALC...{'#'*3}")

weight = input("Enter weight in Kg: ")
height = input("Enter height in metres: ")

weight = int(weight)
height = float(height)

sqr_height = math.sqrt(height)

bmi = weight/sqr_height
bmi = int(bmi)

print(f"Your BMI Calculation is: {bmi}.")