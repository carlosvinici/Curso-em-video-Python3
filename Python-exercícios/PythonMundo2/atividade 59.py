print('='*5, 'PA', '='*5)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p
cont = 1
while cont <= 10:
    print('{}_'.format(termo), end='')
    cont += 1
    termo += r
print('\nFIM')