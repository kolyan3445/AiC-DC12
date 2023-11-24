"""Вычислить сумму знакопеременного ряда -(|х(3n-1)|)/(3n-1)!, где х-матрица ранга к (к и матрица задаются
случайным образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков
после запятой. У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого  +."""
import math
import random
import numpy as np
from decimal import Decimal, getcontext


flag = 0
precision = input('Введите число t > 0: ')  # Ввод и проверка введёного числа знаков после запятой

while True:
    try:
        precision = int(precision)
    except ValueError:
        print('Ошибка: введено не число. Повторите ввод.')
        precision = None
    finally:
        if precision is None:
            pass
        elif float(precision) < 0:
            print('Ошибка: число меньше нуля. Повторите ввод.')
        elif int(precision) == 0:
            flag = 1
            break
        else:
            getcontext().prec = precision
            break
    precision = input('Введите число t > 0:')

matrix_rank = random.randint(1, 10)  # Cоздание и вывод матрицы
matrix_x = np.random.uniform(-1, 1, (matrix_rank, matrix_rank))
print('Матрица x:\n' + str(matrix_x))

n = 1
calculated_matrix = matrix_x
factorial_divisor = 1
curr_answer = 0


# Вычисление суммы знакопеременного ряда
while precision > len(str(curr_answer)):  # Вычисления до t знаков после запятой

    int_current_operator = n * 3 - 1

    calculated_matrix *= (matrix_x ** 3)  # Шаг n: Умножение матриц (возведение в степень)
    factorial_divisor *= -1 * (int_current_operator - 1) * (int_current_operator - 2)  # Шаг n: Вычисление знаменателя
    if factorial_divisor == 0:
        factorial_divisor = 1

    # Вычисление слагаемого и добавление к ответу
    curr_answer += -1 * (Decimal(np.linalg.det(calculated_matrix))) / Decimal(factorial_divisor)

    n += 1  # Вычисление следующего числа

if flag == 1:
    curr_answer = math.ceil(float(curr_answer))

print('Ответ: ' + str(curr_answer))
