# Positional Arguments vs Keyword Arguments

a = 3
b = 9
c = 27

# Values must be passed in when called
def positional_arg(a, b, c):
    print("This is a positional argument")
    print(f"Values:\na:{a}\nb:{b}\nc:{c}")

# Values are predefined before the function is called
def keyword_arg(a=1,b=2,c=3):
    print("This is a keyword argument")
    print(f"a:{a}\nb:{b}\nc:{c}")

# Call the functions
positional_arg(a, b, c)

# This call does not require parameters to be passed in as they are already defined
keyword_arg()