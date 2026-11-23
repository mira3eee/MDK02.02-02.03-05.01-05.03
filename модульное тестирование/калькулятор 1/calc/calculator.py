import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def power(a, b):
    result = a ** b
    if isinstance(result, complex):
        raise ValueError("Результат не является действительным числом")
    return result


def square_root(a):
    if a < 0:
        raise ValueError("Нельзя извлечь квадратный корень из отрицательного числа")
    return math.sqrt(a)


def factorial(a):
    if not isinstance(a, (int, float)) or not float(a).is_integer():
        raise ValueError("Факториал определён только для целых чисел")
    if a < 0:
        raise ValueError("Факториал отрицательного числа не определён")
    return math.factorial(int(a))


def memory_store(memory, value):
    memory["value"] = value


def memory_read(memory):
    return memory.get("value", 0)


def memory_add(memory, value):
    memory["value"] = memory_read(memory) + value


def memory_clear(memory):
    memory["value"] = 0
