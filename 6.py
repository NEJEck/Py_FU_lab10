"""
XOR.
Булева функция XOR (сложение по модулю два) задаётся следующей таблицей истинности:
xor(0,0)=0
xor(0,1)=1
xor(1,0)=1
xor(1,1)=0
На вход подаются две последовательности (a1,…,an) и (b1,…,bn) из 0 и 1.
Вычислите последовательность из (c1,…,cn), где каждая cᵢ=xor(aᵢ,bᵢ).
"""
print(*list(map(lambda xy: (xy[0] + xy[1]) % 2, zip(map(int, input().split()), map(int, input().split())))))
