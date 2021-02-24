from random import randint
pc = randint(1, 5)
print('=='*2,'Jogo da adivinhação','=='*2,)
num = 0
palpites = 0
while num != pc:
    player = int(input('\nDe 0 a 5\nQual número eu pensei?: '))
    num += player
    palpites += 1
    if num == pc:
        print('Você acertou!!!!! eu pensei no numero {} mesmo!!'.format(pc))
        print('palpites necessarios {}'.format(palpites))
        print('=='*15)
    elif player > 5:
        print('Entre 0 e 5! tente novamente!')
        print('=='*15)
    else:
        print('Você errou... :( tente novamente!')
        print('=='*15)

