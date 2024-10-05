first = int(input('1 '))
second = int(input('2 '))
third = int(input('3 '))
if first == second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')
