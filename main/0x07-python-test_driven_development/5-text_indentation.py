#!/usr/bin/python3
"""module contains a function that prints a text"""


def text_indentation(text):
    """a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): string to be printed

    Raises:
        TypeError: if text is not a string
    """
    word = ""
    char_list = ['.', '?', ':']
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        word += text[i]
        if text[i] in char_list:
            word += '\n'
            word += '\n'
    print(word)
