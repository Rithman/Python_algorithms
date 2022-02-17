# Write a function that reverses a string. The input string is given as an array of characters.

def reverse_srt(string: str):
    def sub_func(str, idx):
        if idx >= len(str):
            return
        sub_func(str, idx + 1)
        print(str[idx], end='')

    sub_func(string, 0)


reverse_srt('asdf')
