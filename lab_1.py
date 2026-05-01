""" Лабораторная работа 1, вариант 4"""

import itertools

try:
    n = int(input("Введите n (от 1 до 7): "))

    if n > 7:
        print("Ошибка: n не должно превышать 7")
    elif n < 1:
        print("Ошибка: n должно быть натуральным числом")
    else:
        # range создает список от 1 до n
        numbers = list(range(1, n + 1))
        # itertools.permutations возвращает итератор со всеми вариантами
        all_numbers = list(itertools.permutations(numbers))

        print(len(all_numbers))
        # Выводим каждую перестановку, разделяя числа пробелом
        for p in all_numbers:
            print(*p)

except ValueError:
    print("Ошибка: введите целое число")
