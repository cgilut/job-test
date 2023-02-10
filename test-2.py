# Задача 2
# Написать метод/функцию, который/которая на вход принимает число (float), а на выходе получает число, округленное до пятерок.
# Пример:
# 27 => 25, 27.8 => 30, 41.7 => 40.

def round_to_nearest_5(float_input, base = 5):
    return base * round(float_input/base)

float_input = None

# Проверяем, является ли введенное значение числом, если нет, то выдаем ошибку и просим попробовать еще раз
while float_input is None:
    user_input = input("Пожалуйста, введите число: ")
    try:
        float_input = float(user_input)
    except ValueError:
        print("Ошибка, введенное значение не является числом.")

print(round_to_nearest_5(float_input))

# Время выполнения 15-20 минут