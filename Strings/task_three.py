def replacer(s: str) -> str:
    """
    Add your code here
    """
    # s = s.replace("'", '"')
    # s = s.replace("'", '"')
    s = s.replace("'", "§")
    s = s.replace('"', "'")
    s = s.replace("§", '"')

    return s


print(replacer("He said: 'Hi' and then 'Bye'"))