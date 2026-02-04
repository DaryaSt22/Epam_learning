# Functions. Decorators. Final Task 1.
# Implement a function that works the same as str.split method (without using str.split itself, ofcourse). Pay attention to strings with multiple spaces. For example: ' Hi Python world!'
#
# Example:
#
#     def split(data: str, sep=None, maxsplit=-1):
#         ...


from typing import List


def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here
    """
    if data == '' and sep is None:
        return []
    elif maxsplit == 0:
        if sep is None:
            trimmed = data.strip()
            return [] if trimmed == '' else [trimmed]
        else:
            return [data]
    elif maxsplit != 0:
        result = []
        current_chars = []
        for char in data:
            if char.isspace():
                if current_chars:
                    word = ''.join(current_chars)
                    result.append(word)
                    current_chars.clear()
                    continue
            current_chars.append(char)
            if current_chars:
                result.append(''.join(current_chars))
        return result


# if __name__ == '__main__':
#     assert split('') == []
#     assert split(',123,', sep=',') == ['', '123', '']
#     assert split('test') == ['test']
#     assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
#     assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
#     assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
#     assert split('    set   3     4') == ['set', '3', '4']
#     assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
#     assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

print(split('') == [])
print(split(',123,', sep=',') == ['', '123', ''])
print(split('test') == ['test'])
print(split('Python    2     3', maxsplit=1) == ['Python', '2     3'])
print(split('    test     6    7', maxsplit=1) == ['test', '6    7'])
print(split('    Hi     8    9', maxsplit=0) == ['Hi     8    9'])
print(split('    set   3     4') == ['set', '3', '4'])
print(split('set;:23', sep=';:', maxsplit=0) == ['set;:23'])
print(split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23'])
