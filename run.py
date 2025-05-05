import random

DOGS= ["Alsatian", "Collie"]
CARS = ["Mercedes", "Jaguar"]
NAMES = ["Hugh", "Cora"]

def main():
    print("Welcome to Hangman, everyone's favourite word guessing game!")
    print("The rules are simple; after selecting a category," 
            "you will be given a random word.")
    print("You can then begin guessing letters in that word." 
            "If you guess wrongly 5 times, you lose.")
    print("To begin, please choose a category:")
    print("Dogs")
    print("Cars")
    print("Names")

    category = str(input())
    if category == "Dogs":
        challenge = random.sample(DOGS, 1)
    elif category == "Cars":
        challenge = random.sample(CARS, 1)
    elif category == "Names":
        challenge = random.sample(NAMES, 1)


main()