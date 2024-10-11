numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = False
for i in numbers:
    y = i - 1
    if is_prime == True:
        prime.append(y)
    elif i == 2:
        prime.append(i)
    elif i == 1:
        continue
    y = i + 1
    for j in range(2 , y):
        y = i
        x = i % j
        if i == j:
            break
        elif x == 0:
            is_prime = False
            not_prime.append(y)
            break
        else:
            is_prime = True
        continue
print('Prime:' ,prime)
print('Not_prime:' ,not_prime)

