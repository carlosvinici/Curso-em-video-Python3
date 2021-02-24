casa = float(input('Digite o valor da casa: '))
salario = float(input('Qual o valor da sua renda mensal: '))
anos = float(input('Em quantos anos você quer financiar a casa? '))
meses = anos * 12
if casa / meses >= 0.30 * salario:
    print('\033[1;31m--'*15)
    print('Sua renda é insuficiente :(')
    print('--'*15)
else:
    print('\033[1;32m--'*35)
    print('Parabens!! Você foi aprovado! O valor da parcela ficará {:.2f} por mês'.format(casa / meses))
    print('--'*35)




