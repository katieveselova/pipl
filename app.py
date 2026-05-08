def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # Здесь скрытая ошибка: деление на ноль

if __name__ == "__main__":
    print(add(2, 3))
