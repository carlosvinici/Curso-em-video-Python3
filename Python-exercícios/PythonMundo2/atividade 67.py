'''CÓDIGO DO PROFESSOR '''
from random import randint
print('==' * 5, 'Vamos jogar ipar / par', '==' * 5)
v = 0
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 10)
    total = computador + jogador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}, total de {total} ', end=' p')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente')
print(f'Game over! você venceu {v}.')

''' MEU CÓDIGO PARA O PROBLEMA:

contv = 0
contd = 0
while True:
    jogador = int(input('Digite sua jogada de 1 a 10: '))
    escolha = str(input('I/P ? '))
    maquina = randint(1, 10)
    soma = maquina + jogador
    if soma % 2 == 0 and escolha in 'Ii':
        contd += 1
        print(f'você perdeu, jogaste {jogador} e a maquina {maquina} resultando {soma} PAR \n{contv} vitorias, {contd} derrotas')
        break
    if soma % 2 != 0 and escolha in 'Pp':
        contd += 1
        print(f'você perdeu, jogaste {jogador} e a maquina {maquina} resultando {soma} IMPAR \n{contv} vitorias, {contd} derrotas')
        break
    if soma % 2 == 0 and escolha in 'Pp':
        contv += 1
        print(f'você ganhou, jogaste {jogador} e a maquina {maquina}resultando {soma} PAR \n{contv} vitorias, {contd} derrotas')
    if soma % 2 != 0 and escolha in 'Ii':
        contv += 1
        print(f'você ganhou, jogaste {jogador} e a maquina {maquina} resultando {soma} IMPAR \n{contv} vitorias, {contd} derrotas')
print('acabou')'''