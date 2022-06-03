def main():
    print("Opening Odd or Even Calculator")

    while True:
        calculate_odd_even()

def calculate_odd_even():
    user_input = int(input("Enter a number\n"))

    if user_input % 2 == 0:
        print(f"\n{user_input} is an even number")
    else:
        print(f"\n{user_input} is an odd number")

# Run main
main()