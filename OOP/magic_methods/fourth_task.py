# You have to implement class Book with attributes price, author, name.
#
# author and name fields have to be immutable;
# price field may be changes but has to be in 0 <= price <= 100 range.
# If user tries to change author or name fields after initialization or set price out of range, the ValueError should be raised.
#
# Implement descriptors PriceControl and NameControl to validate parameters.
#
# Example
# >>> b = Book("William Faulkner", "The Sound and the Fury", 12)
# >>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
# Author='William Faulkner', Name='The Sound and the Fury', Price='12'
#
# >>> b.price = 55
# >>> b.price
# 55
# >>> b.price = -12  # => ValueError: Price must be between 0 and 100.
# >>> b.price = 101  # => ValueError: Price must be between 0 and 100.
#
# >>> b.author = "new author"  # => ValueError: Author can not be changed.
# >>> b.name = "new name"      # => ValueError: Name can not be changed.


class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError("Price must be between 0 and 100.")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.storage_name]

    def __set_name__(self, owner, name):
        self.storage_name = "_" + name


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __set__(self, instance, value):
        if self.storage_name not in instance.__dict__:
            instance.__dict__[self.storage_name] = value
        elif self.field_name == 'author':
            raise ValueError("Author can not be changed.")
        else:
            raise ValueError("Name can not be changed.")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.storage_name]

    def __set_name__(self, owner, name):
        self.field_name = name
        self.storage_name = "_" + name


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price