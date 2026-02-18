# Write a function divide which accepts a string that contains two integers, separated by spaces (integers can be separated by more than one space). You have to perform the division operation (a / b) and return the result (float) or an error message.
#
# The structure of the error message is the following: Error code: {error message}.
#
# Example
# >>> divide("4 2")
# 2.0
#
# >>> divide("4 0")
# "Error code: division by zero"
#
# >>> divide("* 1")
# "Error code: invalid literal for int() with base 10: '*'"


def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    try:
        a_str, b_str = str_with_ints.split()
        divide_parts = int(a_str) / int(b_str)
        return divide_parts
    except Exception as e:
        return f"Error code: {e}"

print(divide("4 2"))
print(divide("4 0"))
print(divide("* 1"))
