def sum_value(numbers):
def max_value(numbers):
    """ This function returns the largest number in the list. """
    max_num = numbers[0]   # берём первый элемент как максимум
    for num in numbers:    # проходим по всем элементам
        if num > max_num:  # если нашли больше
            max_num = num
    return max_num
    """ This function returns the largest number
        in the list.
    """
    
    num1 = 2
    num2 = 3
    sum = num1 + num2


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
