# Задача 1
# Написать метод/функцию, который/которая на вход принимает массив городов. В качестве результата возвращает строку, где города разделены запятыми, а в конце стоит точка. 
# Пример:
# «Москва, Санкт-Петербург, Воронеж.» 

def city_list():
    # Запрашиваем количество городов
    number_of_cities = int(input("Пожалуйста, укажите количество городов в массиве: "))
    array_city= []
    # Заполняем массив названиями городов
    for i in range(number_of_cities):
        city = input("Пожалуйста, введите название города: ")
        array_city.append(city)
    
    # Разделяем названия запятыми, в конце ставим точку
    string_city = ""
    for i in range(len(array_city)):
        if i == len(array_city) - 1:
            string_city += array_city[i] + "."
        else:
            string_city += array_city[i] + ", "
    return string_city

print(city_list())

# Время выполнения 15-20 минут