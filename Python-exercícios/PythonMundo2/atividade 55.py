maioridade = 0
totmulher = 0
mediaidade = 0
nomemaior = ''
soma = 0
maiormulher = 0
for p in range(1, 5):
    print('=='*3, '{}º Pessoa'.format(p),'=='*3)
    nome = str(input('Qual seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu Sexo F/M:'))
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomemaior = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomemaior = nome
    if sexo in 'Ff' and idade > 20:
        totmulher += 1
        maiormulher = nome
mediaidade = soma / 4
print('A idade media do grupo é {} anos'.format(mediaidade))
print('O {} é o homem mais velho com {} anos'.format(nomemaior, maioridade))
print('Mulher(es) maior(es) de idade {}, são elas {}'.format(totmulher, maiormulher))
