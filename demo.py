odd = 1
number = int(input('Enter an integer: '))
while odd != number:
    print(odd)
    if number > 0:
        odd += 2
    else:
        odd -= 2

print('Finished')