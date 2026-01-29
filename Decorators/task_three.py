# Functions. Decorators. Decorators. Task 3.
# Create decorator validate which validates arguments in set_pixel function.
# All function parameters should be between 0(int) and 256(int) inclusive.
#
# In case if all parameters are valid, set_pixel function should
# return "Pixel created!" message. Otherwise, it should return "Function call is not valid!" message.
#
# Use functools.wraps where is it necessary.
#
# Don't forget about doc stings.
#
# Examples
# >>> set_pixel(0, 127, 300)
# Function call is not valid!
# >>> set_pixel(0,127,250)
# Pixel created!

def validate(fn):
    '''
    Add corresponded arguments and implementation here.
    '''

    def wrapper(*args, **kwargs):
        is_valid = True
        for arg in args:
            if not isinstance(arg, int) or not (0 <= arg <= 256):
                is_valid = False
        for value in kwargs.values():
            if not isinstance(value, int) or not (0 <= value <= 256):
                is_valid = False
        if is_valid:
            return fn(*args, **kwargs)
        else:
            return "Function call is not valid!"

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"