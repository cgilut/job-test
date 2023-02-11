# Задача 5
# Написать метод, который определяет, какие элементы присутствуют в двух экземплярах в каждом из массивов (= в двух и более, причем в каждом).
# На вход подаются два массива. На выходе массив с необходимыми совпадениями.
# Пример:
# [7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1]
# На выходе [1, 17]

def common_duplicates_in_arrays(array1, array2):

    result_array = []

# Считаем сколько раз каждый элемент повторяется в каждом массиве
    for n in array1:
        duplicate_values_array1 = array1.count(n)
        duplicate_values_array2 = array2.count(n)
        # Элементы, которые присутствуют в 2+ экземплярах в каждом массиве добавляются в результат
        if duplicate_values_array1 >= 2 and duplicate_values_array2 >= 2:
            result_array.append(n)

    # Удаляем дубликаты        
    result_array = sorted(set(result_array))
    print("Совпадения: ", result_array)
    return result_array

common_duplicates_in_arrays([7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 23, 1, 8, 1])

# Время выполнения 60 минут