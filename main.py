import csv
import os
import random


def main():
    FILENAME = "flashcards.csv"
    # make sure file exists
    initial_file(FILENAME)
    # start app
    while True:
        print("Welcome to KoalaCards!")
        print("1. Practice flashcards")
        print("2. Add new flashcards")
        print("3. Exit")

        # get user's choice
        try:
            choice = int(input("Choose an option above! (1, 2, 3): "))
            # Start practice
            if choice == 1:
                flashcards = load_flashcards(FILENAME)
                # check if there are any flashcards
                if flashcards:
                    # ask a user whether to shuffle cards
                    shuffle_input = input("Shuffle cards? (y/n): ").lower()
                    # if a user says 'y' shuffle cards
                    if shuffle_input == "y":
                        random.shuffle(flashcards)
                    wrong_cards = run_flashcards(flashcards)
                    while wrong_cards:
                        retry_input = input("\nRetry cards with incorrect answer? (y/n): ").lower()
                        if retry_input == 'y':
                            wrong_cards = run_flashcards(wrong_cards)
                        else:
                            break
                else:
                    print("------------------------------------")
                    print("No flashcards found! Add some first.")
                    print("------------------------------------")
            # run add_flashcards function
            elif choice == 2:
                add_flashcards(FILENAME)
            # quit
            elif choice == 3:
                print('--------------------')
                print("Thanks for playing!")
                print("Goodbye!")
                print('--------------------')
                break
            # any other number that is not in (1, 2, 3)
            else:
                print("--------------------------")
                print("Invalid choice! Try again.")
                print("--------------------------")
        except:
            print("------------------------------------------------")
            print("Incorrect input. Choose only between 1, 2 and 3.")
            print("------------------------------------------------")

        

# create a csv file
def initial_file(filename):
    # check if the filename  doesn't exist
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["front", "back"])
            writer.writeheader()


# function to load flashcards from csv
def load_flashcards(filename):
    # create an array to store cards
    flashcards = []
    # open and load flashcards
    with open(filename, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        # iterate through reader and add info to flashcards
        for row in reader:
            flashcards.append({"front": row["front"], "back": row["back"]})

    return flashcards


# function to let user create their own cards
def add_flashcards(filename):
    print("\nAdd new flashcards (type 'q' to quit at any time)\n")
    # open the csv file in the append mode
    with open(filename, mode="a", newline="") as csvfile:
        fieldnames = ["front", "back"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # asking to fill cards
        while True:
            front = input("Enter the question: ")
            if front.lower() == "q":
                break
            back = input("Enter the answer: ")
            if front.lower() == "q":
                break

            # add cards to the file
            writer.writerow({"front": front, "back": back})
            print("-------------------")
            print("Flashcard added!")
            print("-------------------")


# show flashcards one by one
def run_flashcards(flashcards):
    # set score and wrong answers arrays
    score = 0
    wrong_cards = []

    # loop over flashcards
    for i, c in enumerate(flashcards, 1):
        print(f"\nCard {i}/{len(flashcards)}")
        # get question and answer
        q = c["front"]
        a = c["back"]
        # ask question
        print(f"{q}")
        # get user's answer
        user_answer = input("Your answer: ")
        # clean user's answer
        clean_user_answer = user_answer.strip().lower().replace(" ", "")
        # clean answer
        clean_a = c["back"].strip().lower().replace(" ", "")
        # compare answers
        if clean_user_answer == clean_a:
            # add +1 to the score
            score += 1
            print("That's right!")
        else:
            # add the card to cards with wrong answer
            wrong_cards.append(c)
            print(f"That's incorrect! The answer is {a}")
    
    # print output
    print("-------------------------------------------")
    print(f"You got {score}/{len(flashcards)} cards right!")
    print("-------------------------------------------")
    return wrong_cards


if __name__ == "__main__":
    main()
