"""
Задание №2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def func(data):
    res = sorted(list(set([ord(el) for el in data])), reverse=True)
    return res


data = input("Введите строку текста: ")
print(func(data))
