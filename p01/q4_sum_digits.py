integer = int(input("Enter an integer between 0 to 1000: "))
one = integer % 10
quotient_1 = integer // 10
tenth = quotient_1 % 10
hundredth = quotient_1 // 10
sum_digits = one + tenth + hundredth

if integer < 0 or integer > 1000:
    print("Please choose an integer between 0 to 1000.")
elif integer == 1000:
    print("The sum of the digits in your integer is 1.")
else:
    print("The sum of the digits in your integer is", sum_digits)
