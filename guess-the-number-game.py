import random
print("Welcome to the number guessing game you will be given 3 chances")
print("\n")
for x in range(0,3):
    guessed_number= int(input("Enter number you think will come : "))
    if guessed_number in range(0,11):
        number = random.randint(0,10)
        if guessed_number == number:
            print("The number is", number)
            print("You guessed it right, you won !")
        else:
            print("The number is",number)
            print("Sorry, you guessed the wrong number")
            print("\n")
    else:
        print("Please enter a number between 0 to 10")
print("Thank you for playing")