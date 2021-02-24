n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menos que {}'.format(n1, n2))
elif n1 == n2 or n2 == n1:
    print('{} e o {} são iguais'.format(n1, n2))



