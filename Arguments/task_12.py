# 12. Обязательный именованный аргумент (логикой)
# Напиши функцию log(message, level="INFO"), печатающую:
# "[LEVEL] message".
# Вызови её так, чтобы из кода было понятно, за что отвечает level (используй именованный аргумент).

def log(message, level="INFO"):
    print(f"[{message}] {level}")

log(message="Lol", level="INFO")