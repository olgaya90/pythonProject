"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
"""
a = int(input('Введите строронну а: '))
b = int(input('Введите строронну b: '))
c = int(input('Введите строронну c: '))
if a + b < c or a + c < b or b + c < a:
    print('Треугольник не существует')
else:
    print('Треугольник существует')
    if a == b != c or a == c != b or c == b != a:
        print('И является равнобедренный треугольник')
    elif a == b == c:
        print('И является равнобедренный равносторонним треугольником')
    else:
        print('И является равнобедренный разносторонним треугольником')