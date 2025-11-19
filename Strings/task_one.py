def get_fractions(a_b: str, c_b: str) -> str:
    """
    Add your code here
    """

    a_num_str, a_den_str = a_b.split("/")
    c_num_str, c_den_str = c_b.split("/")
    a_num = int(a_num_str)
    c_num = int(c_num_str)
    den = a_den_str
    sum_num = a_num + c_num
    result_str = f"{a_b} + {c_b} = {sum_num}/{den}"
    return result_str

a_b = "1/3"
c_b = "5/3"
print(str(get_fractions(a_b, c_b)))
