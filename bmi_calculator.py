height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = weight / height ** 2
if bmi < 18.5:
    print(f"Your bmi is {bmi} is hence you are underweight")
elif (bmi < 25) and (bmi > 18.5):
    print(f"Your bmi is {bmi} is hence you are normal")
elif (bmi < 30) and (bmi > 25):
    print(f"Your bmi is {bmi} is hence you are Overweight")
elif bmi > 30:
    print(f"Your bmi is {bmi} is hence you are obese")

