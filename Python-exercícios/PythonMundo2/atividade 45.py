from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('\033[1;31m='*10,'JOKENPÔ', '='*10)
jogador = int(input('''\033[1;32mEscolha sua jogada
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Sua jogada: '''))
print('\033[1;31m='*29)
print('''jogador: {}
pc: {}'''.format(itens[jogador], itens[pc]))
if jogador == 0:
    if pc == 0:
        print('EMPATE!!')
    elif pc == 1:
        print('Você venceu!!')
    elif pc == 2:
        print('Você Perdeu!!')
elif jogador == 1:
    if pc == 0:
        print('Você venceu!!')
    elif pc == 1:
        print('EMPATE!!')
    elif pc == 2:
        print('Você perdeu!!')
elif jogador == 2:
    if pc == 0:
        print('Você perdeu!!')
    elif pc == 1:
        print('você venceu!!')
    elif pc == 2:
        print('EMPATE!!')
else:
    print('COMANDO INVALIDO')