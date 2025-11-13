# ax2 + bx + c == 0
from math import sqrt

#a = float(input(("a: ")))
#b = float(input("b: "))
#c = float(input("c: "))

def determinant(a: float, b: float, c: float):

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = ((-b + sqrt(discriminant)) / (2*a))
        x2 = ((-b - sqrt(discriminant)) / (2*a))
        return x1, x2
    elif discriminant == 0:
        x = (-b) / (2*a)
        return (x,)
    else:
        return None

print(determinant(1, 6, 5))
print(determinant(1, 4, 4))
print(determinant(1, 6, 45))