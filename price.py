# ФУНКЦИИ
# Создайте в редакторе файл price.py
# Создайте функцию format_price, которая принимает один аргумент price
def format_price(price):
    # Приведите price к целому числу (тип int)
    price = int(price)
    # Верните строку "Цена: ЧИСЛО руб."
    result = f'Цена: {price} руб.'
    return result

# Вызовите функцию, передав на вход 56.24 и положите результат в переменную 
new_price = format_price(56.24)
# Выведите значение переменной с результатом на экран
print(new_price)











