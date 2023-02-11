# Задача 4
# Написать метод/функцию, который/которая на вход принимает целое число, а на выходе возвращает то, 
# является ли число простым (не имеет делителей кроме 1 и самого себя).

def is_it_a_prime_number(integer_input):
    return integer_input

integer_input = None

# Проверяем, является ли введенное значение числом, если нет, то выдаем ошибку и просим попробовать еще раз
while integer_input is None:
    user_input = input("Пожалуйста, введите целое, положительное число: ")
    try:
        integer_input = int(user_input)
        # Проверка на положительное число
        if integer_input < 1:
            print("Ошибка, введенное число не является положительным.")
            integer_input = None
    except ValueError:
        print("Ошибка, введенное значение не является целым числом.")

# Делим введенное значение на каждое число от 2 до самого себя
k = 2

while True:
    if integer_input % k == 0 and integer_input != k or integer_input == 1:
        print("Число " + str(integer_input) + " не является простым.")
        break
    if integer_input % k == 0 and integer_input == k:
        print("Число " + str(integer_input) + " является простым.")
        break
    else:
        k += 1

# Время выполнения 40 минут