import random

DOGS = ["Alsatian", "Collie"]
CARS = ["Mercedes", "Jaguar"]
NAMES = ["Hugh", "Cora"]

CHALLENGE = []

def choose_category():
    print("To begin, please choose a category:")
    print("DOGS")
    print("CARS")
    print("NAMES")

    category = str(input().upper())

    while True:
        if category == "DOGS":
            CHALLENGE.append(random.sample(DOGS, 1))
            gameboard()
            break
        elif category == "CARS":
            CHALLENGE.append(random.sample(CARS, 1))
            gameboard()
            break
        elif category == "NAMES":
            CHALLENGE.append(random.sample(NAMES, 1))
            gameboard()
            break
        else:
            print("Please choose a category to begin")

def gameboard():
    board = []
    for i in range(len(CHALLENGE[0])):
        board.append(i)
        print(board)

def main():
    print("Welcome to Hangman, everyone's favourite word guessing game!")
    print("The rules are simple; after selecting a category," 
            "you will be given a random word.")
    print("You can then begin guessing letters in that word." 
            "If you guess wrongly 5 times, you lose.")
    choose_category()


main()