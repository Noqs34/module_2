my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
print(len(my_list))
while len(my_list) > a:
    if my_list[a] > 0:
        print(my_list[a])
        a = a + 1
        continue
    else:
        a = a + 1
        continue