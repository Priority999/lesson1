# Добавьте словарь
moscow_dict = {
    "city": "Москва",
    "temperature": "20"    
}
# Выввдите на экран значение ключа 'city'
print(moscow_dict["city"])

# Уменьшите значение 'temperature' на 5
moscow_dict["temperature"] = "15"
# Выведите на экран весь словарь
print(moscow_dict)

# Проверьте, есть ли в словаре ключ country
print(moscow_dict.get('country')) #None

# Выведите значение по-умолчанию "Россия" для ключа country
print(moscow_dict.get('country', 'Россия'))

# Добавьте в словарь элемент date со значение  "27.05.2019"
moscow_dict['date'] = "27.05.2019"

# Выведите на экран длину словаря 
print(len(moscow_dict))


