def main():
    # A single string
    values = "1 2 3 4 5"
    print(values)

    # The split() method splits a string into a list.
    # You can specify the separator, default separator is any whitespace.
    v_list = values.split()
    
    # show list
    print(v_list)

    # sum up the values
    total = 0
    for value in v_list:
        total += int(value)

    # find the length of the list
    list_length = 0
    for value in v_list:
        list_length += 1

    # find average value
    average_value = total/list_length
    print(f"Average Value: {average_value}")

main()