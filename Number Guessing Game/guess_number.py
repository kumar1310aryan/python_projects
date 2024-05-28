import random

def game():

    ans=random.randint(0,100)
    attempts=0

    print("Welcome!!")
    print("Guess a number bw 0 and 100")
    print("Try to guess it!!")

    while True:
        try:
            guess=int(input("Enter your no. "))
            attempts+=1;
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
            elif guess < ans:
                print("Too low! Try again.")
            elif guess > ans:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                break


        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    
game()