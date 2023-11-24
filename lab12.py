"""Вычислить сумму знакопеременного ряда -(|х(3n-1)|)/(3n-1)!, где х-матрица ранга к (к и матрица задаются
случайным образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков
после запятой. У алгоритма д.б. линейная сложность. Операция умножения –поэлементная. Знак первого слагаемого  +."""
import math
import random
import numpy as np
from decimal import Decimal, getcontext


def precision_point(number_to_count):  # Функция подсчёта кол-ва знаков после запятой
    return Decimal(number_to_count).as_tuple().exponent * (-1)


flag = 0
precision = input('Введите число t > 0 (кол-во знаков после запятой): ')  # Ввод и проверка введёного числа знаков после запятой

while True:
    try:
        precision = int(precision)
    except ValueError:
        print('Ошибка: введено не число. Повторите ввод.')
        precision = None
    finally:
        if precision is None:
            pass
        elif precision < 0:
            print('Ошибка: число меньше нуля. Повторите ввод.')
        elif precision == 0:
            flag = 1
            break
        else:
            getcontext().prec = precision # Увеличение глубины Decimal
            break
    precision = input('Введите число t > 0:')

matrix_rank = random.randint(1, 10)  # Cоздание и вывод матрицы
matrix_x = np.random.uniform(-1, 1, (matrix_rank, matrix_rank))
print('Матрица x:\n' + str(matrix_x))

n = 1
calculated_matrix = matrix_x
factorial_divisor = None
curr_answer = 0


# Вычисление суммы знакопеременного ряда
while precision_point(curr_answer) < precision:  # Вычисления до t знаков после запятой
    int_current_operator = n * 3 - 1

    if int_current_operator == 2:
        calculated_matrix *= matrix_x  # Шаг 1: Умножение матриц (возведение в степень)
        factorial_divisor = 2  # Шаг 1: Вычисление знаменателя

    else:
        calculated_matrix *= (matrix_x ** 3)  # Шаг n: Умножение матриц (возведение в степень)
        factorial_divisor *= (int_current_operator - 1) * (int_current_operator - 2) # Шаг n: Вычисление знаменателя

    # Вычисление слагаемого и добавление к ответу
    if n % 2 == 1:
        curr_answer += \
            -1 * (Decimal(np.linalg.det(calculated_matrix))) / Decimal(factorial_divisor)
    else:
        curr_answer -= \
            -1 * (Decimal(np.linalg.det(calculated_matrix))) / Decimal(factorial_divisor)

    n += 1  # Вычисление следующего числа

if flag == 1:
    curr_answer = math.ceil(float(curr_answer))

print('Ответ: ' + str(curr_answer))
