n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Podem formar um Angulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('não podem formar um angulo')