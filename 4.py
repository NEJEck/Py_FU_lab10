"""
Ноль или не ноль.
Проверьте, есть ли среди данных N чисел нули.
Формат ввода
Вводится число N, а затем N чисел.
"""
from itertools import repeat
print(0 in list(map(lambda r: int(r()), repeat(input, int(input())))))
