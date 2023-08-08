# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться 
# # в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# # Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# # Фраза может состоять из одного слова, если во фразе несколько слов,  то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# # Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

equally = True
vowel = list('а у о ы и э я ю ё е'.split())
# Функция определения суммы гласных во фразе
def separator(x):
    summ = 0
    for i in x:
        for n in vowel:
            if i == n:
                summ += 1
    return summ

# Функция сравнения числа гласных во фразах
def equal(result, equally):
    for i in result:
        if i != result[0] or i == 0:
            equally = False
    if equally == False:
        return "Пам парам"
    else:
        return "Парам пам-пам"

result = equal(list(map(int, map(lambda x: (separator(x)), map(str,input().split())))), equally)
print(result)

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

# 0 * 0 = 0 ----- 0 + 0 = 0

def print_operation_table(operation, num_rows=7, num_columns=7):
    list_columns = list(map(int, range(1, num_columns)))
    list_rows = list(map(int, range(1, num_rows)))
    for i in list_rows:
        list_rowss = list()
        for n in range(1, num_rows):
            list_rowss.append(i)
        result = list(map(operation, list_columns, list_rowss))
        print(result)
eval(input())