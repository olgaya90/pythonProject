#  получаем вводные:
a = float(input())
b = float(input())
c = float(input())

# Квадратное уравнение имеет вид: ax² + bx + c = 0
# Стандартное решение через Дискриминант: D = b2 − 4ac
# если D < 0, корней нет;
# если D = 0, есть один корень;
# если D > 0, есть два различных корня.

# 0.9 Проверяем на <нули>
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
else:

    # 1. Проверяем уравнение на <квадратность>
    if a == 0:
        x = -c / b
        print("{:.2f}".format(round(x, 2)))
    # Уравнение не квадратное

    # 2. Решаем не полные квадратные уравнения
    if b == 0 and c == 0:
        print("{:.2f}".format(round(0, 2)))

    if a != 0 and b == 0 and c != 0:  # x² = - c/а
        if ((- c) / a) < 0:
            print('No solution')  # нет решений
        elif ((-c) / a) > 0:
            agg = abs(c / a) ** 0.5
            ag = agg
            ag2 = -agg
            afk = min(ag, ag2)
            afk2 = max(ag, ag2)
            print(round(afk, 2), round(afk2, 2))

    if a != 0 and b != 0 and c == 0:
        print("{:.2f}".format(0), "{:.2f}".format(round((-b / a), 2)))

    # 3 решаем полное квадратное уравнение:
    # 3.1 Преобразуем неприведенное уравнение в приведенное.
    #  <2x² − 4x— 12 = 0> в <x² − 2x— 6>
    if a > 1:
        b = b / a
        c = c / a
        a = a / a

    # 3.2 решаем полное квадратное уравнение:
    if a != 0 and b != 0 and c != 0:
        d = ((b ** 2) - (4 * a * c))
        if d < 0:
            print('No solution')
        elif d == 0:
            ans1 = -b / 2 * a
            print("{:.2f}".format(round(ans1, 2)))
        else:
            x1 = (-b + d ** 0.5) / (2 * a)
            x2 = (-b - d ** 0.5) / (2 * a)
            prt1 = min(x1, x2)
            prt2 = max(x1, x2)

            if prt1 != prt2:
                print("{:.2f}".format(round(prt1, 2)), "{:.2f}".format(round(prt2, 2)))
            else:
                print("{:.2f}".format(round(prt1, 2))),