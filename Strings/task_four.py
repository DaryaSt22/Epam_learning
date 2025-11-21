def check_str(s: str):
    """
    Add your code here
    """
    s = ''.join(reversed(s))
    return s

print(check_str("Drab as a fool, as aloof as a bard"))



def check_str(s: str):
    """
    Add your code here
    """
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
        return True

print(check_str("malayalam"))



def check_str(s: str):
    """
    Add your code here
    """
    s = ''.join(ch.lower() for ch in s if ch.isalnum())

    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
        return True

print(check_str("No 'x' in Nixon")) # для автопроверки эту строку лучше убрать


def check_str(s: str):
    """
    Add your code here
    """
    s = ''.join(ch.lower() for ch in s if ch.isalnum())

    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True