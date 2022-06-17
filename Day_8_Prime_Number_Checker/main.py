def prime_number_checker(number):
    is_prime = True
    
    # check every number except 1 and the number
    for num in range(2, number):
        if number % num == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

# test function
prime_number_checker(101)
prime_number_checker(99)
prime_number_checker(432783)