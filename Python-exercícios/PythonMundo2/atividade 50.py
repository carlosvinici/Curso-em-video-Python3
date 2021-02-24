'''print('\033[1;35mAperte ENTER para ganhar 1 cm de pau')
for c in range (1, 1000):
    input('\033[1;32mSeu pau ganhou {} cm'.format(c))'''

print('='*22)
print('PROGRESSÃO ARITMETICA')
print('='*22)
p = int(input('Começa: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo, r):
    print(c ,end=' ')