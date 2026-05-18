# 1) User: профиль пользователя
# Условие:
# Нужно описать пользователя системы с базовыми данными и приветствием.
# Что нужно сделать:
# Создай класс User.
# В __init__ принимай username и email.
# Добавь метод greet(), который возвращает строку приветствия (например: Привет, <username>!).
# Добавь метод change_email(new_email) с простой проверкой корректности (например, наличие @).
# Сделай __repr__ или __str__, чтобы объект читабельно выводился.


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f"Hello, {self.username}!"

    def change_email(self, new_email):
        if "@" in new_email:
            self.email = new_email
            return True
        else:
            return False

    def __str__(self):
        return f"Hello, {self.username} {self.email}!"


print(User("John", ""))
print(User("John", "hgrgrub@com"))
