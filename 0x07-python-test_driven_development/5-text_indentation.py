#!/usr/bin/python3

"""write a function that print a text with 2 new lines
after each of these of these 3 characters: . ? :
The text must be a string
There should be no space at the beginning or at the end of each printed line
"""

def text_indentation(text):

    """
    If the text is not a string print :
    TypeError: text must be a string
    """
    new_text = False
    char = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must be a string")
    if len(text) == 0:
        return

    for i in text:
        if new_text and i == ' ':
            new_text = False
        else:
            if i in char:
                print(i, end="")
                print()
                print()
                new_text = True
            else:
                print(i, end="")
