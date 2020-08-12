def find_max(num_list):
    largest = num_list[0]
    for numbers in num_list:
        if numbers > largest:
            largest = numbers
    return largest