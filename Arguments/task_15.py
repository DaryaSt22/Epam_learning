# 15. Совместное использование позиционных и именованных
# Функция booking(destination, days, breakfast=True, spa=False).
# Придумай 3 разных корректных вызова, комбинируя позиционные и именованные аргументы.

def booking(destination, days, breakfast=True, spa=False):
    print(destination, days, breakfast, spa)

booking(days=5, spa=True, breakfast=True,destination="Tallin")
booking("Venece", 9, True, False)
booking("Venece", 9, True, False)
booking("Rome", breakfast=True, days=10, spa=False)