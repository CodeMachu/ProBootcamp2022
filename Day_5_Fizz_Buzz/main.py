def main():
    print("Starting FizzBuzz Calculator\n")
    print("Printing Values...\n")

    for number in range(1, 31):
        if number % 3 == 0 and number % 5 == 0:
            print(f"{number}: FizzBuzz")
        elif number % 3 == 0:
            print(f"{number}: Fizz")
        elif number % 5 == 0:
            print(f"{number}: Buzz")
        else:
            print(f"{number}: ___")

# run main
main()