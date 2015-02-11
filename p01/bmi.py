weight = float(input("Please enter your weight (in kg): "))
height = float(input("Please enter your height (in m): "))
bmi = int(weight/(height*height))
bmi = "{0:.2f}".format(bmi)

if bmi >= "27.5":
    print("Your BMI is", bmi, "and your health risk is high.")
elif bmi >= "23.0" and bmi <="27.4":
    print("Your BMI is", bmi, "and your health risk is moderate.")
elif bmi >=  "18.5" and bmi <= "22.9":
    print("Your BMI is", bmi, "and your health risk is low.")
else:
    print("Your BMI is", bmi, ", risk of nutritional deficiency diseases and osteoporosis.")

