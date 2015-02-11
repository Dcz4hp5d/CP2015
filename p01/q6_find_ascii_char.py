number = int(input("Enter an integer from 0 to 127: "))

if not 0<=number<=127:
    print("Choose an integer from 0 to 127.")
else:
    print("Your alphabet is", chr(number))

