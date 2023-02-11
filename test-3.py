# Задача 3
# Написать метод/функцию, который/которая на вход принимает число (int), а на выходе выдает слово “компьютер” в падеже, соответствующем указанному количеству. 
# Например, «25 компьютеров», «41 компьютер», «1048 компьютеров».

def number_of_computers(integer_input):
    return integer_input

integer_input = None

# Проверяем, является ли введенное значение числом, если нет, то выдаем ошибку и просим попробовать еще раз
while integer_input is None:
    user_input = input("Пожалуйста, введите количество компьютеров: ")
    try:
        integer_input = int(user_input)
    except ValueError:
        print("Ошибка, введенное значение не является целым числом.")

if 5 <= integer_input % 100 <= 20:    
    print(str(number_of_computers(integer_input)) + " компьютеров")
elif integer_input % 10 == 1:
    print(str(number_of_computers(integer_input)) + " компьютер")
elif 2 <= integer_input % 10 <= 4:
    print(str(number_of_computers(integer_input)) + " компьютера")
else:
    print(str(number_of_computers(integer_input)) + " компьютеров")

# Время выполнения 60 минут