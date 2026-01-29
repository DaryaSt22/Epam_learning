# Functions. Decorators. Decorators. Task 2
# Write a decorator which logs information about calls of decorated function,
# values of its arguments, values of keyword arguments and execution time. Log should be written to a file.
#
# Example of using
# @log
# def foo(a, b, c):
#     ...
#
# foo(1, 2, c=3)
# log.txt
# ...
# foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.
# ...
import inspect
import time


def log(fn):
    """
    Add your code here or call it from here
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        return_fn = fn(*args, **kwargs)
        end_time = time.time()
        final_time = end_time - start_time
        name = fn.__name__
        param_names = list(inspect.signature(fn).parameters)
        args_str = ", ".join(f"{n}={v}" for n, v in zip(param_names, args))
        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        line = f"{name}; args: {args_str}; kwargs: {kwargs_str}; execution time: {final_time:.2f} sec."
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(line + "\n")

        return return_fn

    return wrapper