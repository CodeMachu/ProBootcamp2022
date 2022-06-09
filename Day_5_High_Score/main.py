import random

def main():
    print("Generating Random Values List")

    values_list = []

    for x in range(1, 11):
        values_list.append(random.randint(1, 100))

    print(values_list)

    # find highest value
    high_score = 0
    for value in values_list:
        if value > high_score:
            high_score = value

    print(f"\nHigh Score: {high_score}")

# run main
main()