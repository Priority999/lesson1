# ФУНКЦИИ
# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, 
# приводит их к строке и отдает объединенными через разделитель delimiter

def get_summ(one, two, delimiter='&'):
    one = str.upper(one)
    two = str.upper(two)
    delimiter = str(delimiter)
    result = one + delimiter + two
    return result

# Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два параметра, 
# приводит их к строке и отдает объединенными через разделитель delimiter  
print(get_summ("Learn", "Python"))