n = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais outro valor: '))
print('o primeiro valor é:{}'.format(n))
print('o segundo valor é:{}'.format(n2))
print('o terceiro valor é:{}'.format(n3))
menor = n
if n2 < n and n2 < n3:
    menor = n2
if n3 < n and n3 < n2:
    menor = n3
maior = n
if n2 > n and n2 > n3:
    maior = n2
if n3 > n and n3 > n2:
    maior = n3
print('o Menor Numero é {} e o Maior é {}'.format(menor, maior))



