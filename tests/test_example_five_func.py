import doctest

def example_five(words_list_input: list) -> list:
    """
        Функция возвращает список из слов, которые встречались
        в тексте по ходу его чтения слева

        >>> example_five("s s h")
        [0, 1, 0]

        >>> example_five("s s s s h")
        [0, 1, 2, 3, 0]

        >>> example_five("s s r h")
        [0, 1, 0, 0]
    """

    dict_word = {}

    words_list = words_list_input.split(" ")
    count_word_in_words_list = []

    for item_word in words_list:
        dict_word[item_word] = 0

    for i_high, item_word in enumerate(words_list):
        if item_word in words_list[:i_high]:  # хранится история перебора слов
            dict_word[item_word] += 1
        count_word_in_words_list.append(dict_word[item_word])

    return count_word_in_words_list


doctest.testmod()