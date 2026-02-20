# Create a hierarchy out of birds. Implement 4 classes:
#
# class Bird with an attribute name and methods fly and walk.
# class FlyingBird with attributes name, ration, and with the same methods. ration must have a default value. Implement the method eat which will describe its typical ration.
# class NonFlyingBird with same characteristics but which obviously without attribute fly. Add the same "eat" method but with other implementation regarding the swimming bird tastes.
# class SuperBird which can do all of it: walk, fly, swim and eat. But be careful which "eat" method you inherit.
# Implement str() function call for each class.


class Bird:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def fly(self):
        return f"{self.name} bird can fly"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class FlyingBird(Bird):

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird:

    def __init__(self, name, ration='fish'):
        self.name = name
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):



    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"




b = Bird("Any")
print(b.walk())
c = FlyingBird("Canary")
print(str(c))
print(c.eat())
print(SuperBird.__mro__)