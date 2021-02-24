print('+=+'*6, 'Números ', '+=+'* 6 )
soma = cont = maior_num = menor_num = 0
#menor_num = 999
resposta = ''
while resposta in 'S':
    numero = int(input('Digite um número: '))
    resposta = str(input('Você quer continuar? [S/N]: ').upper().strip()[0])
    soma += numero
    cont += 1
    #if numero < menor_num:
        #menor_num = numero
    #elif numero > maior_num:
        #maior_num = numero           Rsp - carlos'''
    if cont == 1:
        menor_num = maior_num = numero
    else:
        if maior_num < numero:
            maior_num = numero
        if menor_num > numero:
            menor_num = numero
media = soma / cont
print('Você digitou {} números, {:.2f} essa foi a média entre eles.'.format(cont, media))
print('O MENOR número digitado é {} e o MAIOR é {}'.format(menor_num, maior_num))
print('Acabou')

