def min_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    min = number[0]

    for num in numbers:
        if num < min:
            min = num

    return min
    
    pass


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
