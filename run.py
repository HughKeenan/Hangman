import random

DOGS= ["Alsatian", "Collie"]
CARS = ["Mercedes", "Jaguar"]
NAMES = ["Hugh", "Cora"]

def choose_category():
    print("To begin, please choose a category:")
    print("Dogs")
    print("Cars")
    print("Names")

    while True:
        category = str(input())
        if category == "Dogs":
            challenge = random.sample(DOGS, 1)
            gameboard()
            break
        elif category == "Cars":
            challenge = random.sample(CARS, 1)
            gameboard()
            break
        elif category == "Names":
            challenge = random.sample(NAMES, 1)
            gameboard()
            break
        else:
            print("Please choose a category to begin")

def gameboard():
    print("Hello, World!")

def main():
    print("Welcome to Hangman, everyone's favourite word guessing game!")
    print("The rules are simple; after selecting a category," 
            "you will be given a random word.")
    print("You can then begin guessing letters in that word." 
            "If you guess wrongly 5 times, you lose.")
    choose_category()


main()