letter = input("Please enter your uppercase letter: ")

if not letter.isalpha():
    print("Please only use a letter from the alphabet.")
elif not len(letter) == 1:
    print('Please only input 1 letter.')
elif letter == letter.lower():
    print("Please enter an uppercase letter.")
else:
    print(letter.lower())
