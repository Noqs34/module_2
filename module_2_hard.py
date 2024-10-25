import math

n = int(input('Введите число от 3 до 20: '))
a = math.ceil(n / 2)
result = []
for i in range(1, a):
    for j in range(1, n):
        if j <= i:
            continue
        x = n % (i + j)
        if x == 0:
            result.append(i)
            result.append(j)
print(*result, sep="")
