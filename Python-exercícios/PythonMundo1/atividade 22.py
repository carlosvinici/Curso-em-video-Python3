from random import randint
sorteado = randint(0, 5)
print('-='*30)
print('Tente adivinhar o número que estou pensando de 0 a 5')
print('-='*30)
n = int(input('É o número:'))
print('processando...')
if n == sorteado:
    print('Acertou!! Você é brabo')
else:
    print('Você errou o número que eu pensei era {} e não {}'.format(sorteado, n))




