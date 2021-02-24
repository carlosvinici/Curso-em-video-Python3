print('-='*20)
print('analisador de triangulos')
print('-='*20)
n = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n < n2 + n3 and n2 < n + n3 and n3 < n2 + n:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos não podem formar um triangulo')
