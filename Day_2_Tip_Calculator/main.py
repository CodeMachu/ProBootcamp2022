def main():
    print("Opening Tip Calculator\n")

    while True:
        calculate_tip()

def calculate_tip():
    print("Calculating new tip...\n")

    bill = float(input("What is the total of your bill?\n$"))

    print("\nWhat percent tip would you like to leave?")
    print(f"1: 10%  (${round((bill * .1), 2)})")
    print(f"2: 15%  (${round((bill * .15), 2)})")
    print(f"3: 20%  (${round((bill * .2), 2)})\n")

    tip_choice = int(input("Enter 1, 2, or 3\n"))

    total = 0

    while total == 0:
        if tip_choice == 1:
            total = round(bill + (bill * .1), 2)
        elif tip_choice == 2:
            total = round(bill + (bill * .15), 2)
        elif tip_choice == 3:
            total = round(bill + (bill * .2), 2)
        else:
            print("Enter a valid selection\n")
            tip_choice = int(input("Enter 1, 2, or 3\n"))

    print(f"\nYour Bill Total is: ${total}\n")


# Run main 
main()