#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    need_trim = False
    for char in text:
        if need_trim and char == " ":
            continue
        need_trim = False
        print(char, end="")
        if char in ".?:":
            print("\n")
            need_trim = True
