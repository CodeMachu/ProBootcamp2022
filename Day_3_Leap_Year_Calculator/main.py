def main():
    print("Opening Leap Year Calculator\n")

    while True:
        calculate_lp()


def calculate_lp():
    user_input = int(input("Enter a year\n"))

    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print(f"{user_input} IS a leap year!\n")
            else:
                print(f"{user_input} is not a leap year\n")
        else:
            print(f"{user_input} IS a leap year!\n")
    else:
        print(f"{user_input} is not a leap year\n")

# Run main
main()