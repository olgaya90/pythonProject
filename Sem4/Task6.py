"""
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def sum_nums(lst, ind_1, ind_2):
    res = 0
    if ind_1 >= ind_2:

        print("Между индексами элементов нет")
        return res
    elif ind_2 >= len(lst):
        return sum(lst[ind_1 + 1:])
    elif ind_1 < 0:
        return sum(lst[:ind_2])
    else:
        return sum(lst[ind_1 + 1: ind_2])


lst = [1, 2, 3, 4, 5]
index_1 = 2
index_2 = 4

print(f"Сумма: {sum_nums(lst, index_1, index_2)}")


def sum_lst(lst_num, index_1, index_2):
    if index_1 >= index_2:
        return 0
    start = max(index_1 + 1, 0)
    stop = min(index_2, len(lst_num))
    return sum(lst_num[start:stop])


lst = [1, 3, -5, 7, 5, 8, 4, -9, 2]
print(f'сумма элементов списка = {sum_lst(lst, -2, 9)}')
print(f'сумма элементов списка = {sum_lst(lst, 3, 6)}')