print('=='*5, 'Mercado Super', '=='*5 )
totmil = barato = totcompra = totcont = 0
resposta = ' '
while resposta not in 'N':
    nome = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: '))
    totcompra += valor
    totcont += 1
    if valor > 1000:
        totmil += 1
    if totcont == 1:
        barato = valor
    else:
        if valor < barato:
            barato = valor
    resposta = str(input('Quer continuar? S/N : ')).upper().strip()[0]
print(f'Total de itens comprados {totcont}')
print(f'itens que custaram mais de mil reais {totmil}')
print(f'Total do valor a ser pago: {totcompra}')
