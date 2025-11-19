def get_longest_word(s: str) -> str:
    """
     Add your code here
    """

    words = s.split()
    longest_world = max(words, key=len)
    return longest_world


# my_string = "Python is simple and effective!"
# print(get_longest_word(my_string))

if __name__ == "__main__":
    my_string = "Python is simple and effective!"
    print(get_longest_word(my_string))