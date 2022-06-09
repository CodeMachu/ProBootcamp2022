import random

def main():
    print("Welcome to Rock, Paper, Scissors!\n")

    while True:
        user_choice = int(input("0: Rock\n1: Paper\n2: Scissors\n\nWhich do you choose?\nEnter a number\n"))

        computer_choice = random.randint(0, 2)

        if user_choice < 0 or user_choice > 2:
            print("Invalid number, computer wins")
        elif user_choice == 0:
            if computer_choice == 0:
                print(f"User: Rock\nComputer: Rock\n")
                print("It's a draw\n")
            elif computer_choice == 1:
                print(f"User: Rock\nComputer: Paper\n")
                print("Computer wins\n")
            else:
                print(f"User: Rock\nComputer: Scissors\n")
                print("User wins!\n")
        elif user_choice == 1:
            if computer_choice == 0:
                print(f"User: Paper\nComputer: Rock\n")
                print("User wins!\n")
            elif computer_choice == 1:
                print(f"User: Paper\nComputer: Paper\n")
                print("It's a draw\n")
            else:
                print(f"User: Paper\nComputer: Scissors\n")
                print("Computer wins\n")
        else:
            if computer_choice == 0:
                print(f"User: Scissors\nComputer: Rock\n")
                print("Computer wins\n")
            elif computer_choice == 1:
                print(f"User: Scissors\nComputer: Paper\n")
                print("User wins!\n")
            else:
                print(f"User: Scissors\nComputer: Scissors\n")
                print("It's a draw\n")

# Run main
main()   