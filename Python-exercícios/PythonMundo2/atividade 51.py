num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('{}'.format(c), end=' ')
        tot += 1
    else:
        print('{}'.format(c), end=' ')
print('\nO numero foi divisivel {} vezes'.format(tot))
if tot == 2:
    print('O numero {} é primo'.format(tot))
else:
    print('ele não é primo')