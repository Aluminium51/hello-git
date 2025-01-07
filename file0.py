print("hello world222")
print("Thailand")

#calculator program
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
operation = input("Enter an operation: ")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Invalid operation")
    
    
# guess the number game
import random
number = random.randint(1, 1000)
guess = None
while guess != number:
    guess = int(input("Guess a number between 1 and 1000: "))
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print("You guessed it! You won!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            number = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break
print("End of program")