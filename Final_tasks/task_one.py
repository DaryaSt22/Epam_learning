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
    if sep == '':
        raise ValueError("empty separator")

    if data == '' and sep is None:
        return []
    if maxsplit == 0:
        if sep is None:
            trimmed = data.strip()
            return [] if trimmed == '' else [trimmed]
        return [data]
    if sep is None:
        result = []
        current_chars = []
        splits_done = 0

        for i, char in enumerate(data):
            if char.isspace():
                if current_chars:
                    word = ''.join(current_chars)
                    result.append(word)
                    current_chars.clear()

                    if maxsplit > 0:
                        splits_done += 1
                        if splits_done == maxsplit:
                            rest = data[i + 1:].lstrip()
                            if rest:
                                result.append(rest)
                            return result
                continue

            current_chars.append(char)

        if current_chars:
            result.append(''.join(current_chars))
        return result


    else:
        result = []
        start = 0
        splits_done = 0
        sep_len = len(sep)
        i = 0

        while i <= len(data) - sep_len:

            if data[i:i + sep_len] == sep:
                result.append(data[start:i])
                start = i + sep_len
                splits_done += 1

                if maxsplit > 0 and splits_done == maxsplit:
                    result.append(data[start:])

                    return result

                i = start
                continue

            i += 1

        result.append(data[start:])

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
