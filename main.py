def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Помилка: {e}")
        return None

expression1 = "2 + 2"
expression2 = "10 / 0"

result1 = calculate(expression1)
result2 = calculate(expression2)

print(f"Результат 1: {result1}")
print(f"Результат 2: {result2}")
