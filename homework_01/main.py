"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]


# filter types
ODD = 'func_odd'
EVEN = 'func_even'
PRIME = 'func_prime'


def filter_numbers(numbers, type_filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type_filter is ODD:
        return func_odd(numbers)
    elif type_filter is EVEN:
        return func_even(numbers)
    else:
        return func_prime(numbers)

def func_odd(o_numbers):
    return list(filter((lambda x: x % 2 != 0), o_numbers))

def func_even(e_numbers):
    return list(filter((lambda x: x % 2 == 0), e_numbers))

def func_prime(pr_numbers):
    result = []
    for pr_number in pr_numbers:
        for num in range(2, pr_number):
            if pr_number % num == 0:
                break
        else:
            result.append(pr_number)
    return result