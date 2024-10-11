numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in numbers:
    if i == 1:
        continue
    for j in range(2 , i):
        y = i
        x = i % j
        if i == j:
            break
        elif x == 0:
            not_prime.append(y)
            break
    else:
        prime.append(i)
print('Prime:' ,prime)
print('Not_prime:' ,not_prime)
