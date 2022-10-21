import random


def min_numb (number_s):
    min_n = number_s[0]
    for i in range(1, len(number_s)):
        if number_s[i] < min_n:
            min_n = number_s[i]
    return min_n


def max_numb (number_s):
    max_n = number_s[0]
    for i in range(1, len(number_s)):
        if number_s[i] > max_n:
            max_n = number_s[i]
    return max_n


def creat_list(n):
    numbers = list()
    for i in range(0,n):
        numbers.append(random.randint(-100,100))
    return numbers


def del_extrem(lst_number, min_n, max_n):
    lst_number.remove(min_n)
    lst_number.remove(max_n)
    return lst_number


while True:
    n = int(input("Введите количество данных \n"))
    if n < 4:
        print("Введено недостаточно данных (количество данных должно быть больше 4-х) \n")
    else:
        lst_number = creat_list(n)
        min_n = min_numb(lst_number)
        max_n = max_numb(lst_number)
        print("Изначальные данные: " + str(lst_number) + "\n")
        lst_no_extremum = del_extrem(lst_number, min_n, max_n)
        print("Итоговая версия списка: " + str(lst_no_extremum))
        break