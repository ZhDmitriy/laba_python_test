import doctest

def example_four(num_list: list) -> int:
    """
        Функция возвращает количество различных чисел в списке

        >>> example_four([1, 1, 2, 3])
        3

        >>> example_four([1, 4, 4, 5, 6, 7])
        5

        >>> example_four([1, 4, 4, 5, 8, 8, 11, 12])
        6

    """
    return len(set(num_list))

doctest.testmod()