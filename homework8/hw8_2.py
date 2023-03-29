import math


# но есть функция abs, которая берет число по модулю не использовала реализованную.
def positive_number(number: int):
    if number < 0:
        return number * -1
    else:
        return number


def if_exist(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False


def triangle_P(a, b, c):
    p = a + b + c
    half_p = p / 2
    return math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))


if __name__ == '__main__':
    i = -1
    while i < 0:
        try:
            side_1 = math.fabs(int(input('Введите длину первой стороны треугольника:')))
            side_2 = math.fabs(int(input('Введите длину второй стороны треугольника:')))
            side_3 = math.fabs(int(input('Введите длину второй стороны треугольника:')))
            i = 0
        except Exception:
            print(f'Не число.Введите число')
            i = -1
    if if_exist(side_1, side_2, side_3) == True:
        print(f'Площадь треугольника {triangle_P(side_1, side_2, side_3)}')
    else:
        print(f'Не треугольник!')
