"""
Задание №6
Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""

from functools import wraps


def deco_param(func):
    dct = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        dct[args[0]] = args[1]
        res = func(args[0], args[1])
        return res, dct

    return wrapper


def func(param):
    def deco(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = f(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return deco


@func(1)
@deco_param
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        print(f'осталось {attempts} попыток')
    return "Не угадал."


#print(attempts_count(15, 2))
print(attempts_count.__name__)