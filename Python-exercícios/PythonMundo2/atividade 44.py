d = float(input('Qual o valor da compra: '))
print('Qual a forma de pagamento?')
print('[ 1 ]À vista dinheiro ou cheque.')
print('[ 2 ]À vista no cartão.')
print('[ 3 ]Em até 2x no cartão.')
print('[ 4 ]Em 3x ou mais no cartão.')
f = int(input('Escolha uma opção: '))
p = d - d * 0.20
s = d - d * 0.05
t = d + d * 0.20
if f == 1:
    print('Comprando á vista com din\cheq você tem desconto de 20%')
    print('Sua compra vai custar: {:.2f}R$'.format(p))
elif f == 2:
    print('Comprando a vistá pelo cartão você tem desconto de 5%')
    print('Sua compra vai custar: {:.2f}'.format(s))
elif f == 3:
    print('Dividindo em 2x no cartão sua comprar ira custar {:.2f}R$/mês'.format(d / 2))
elif f == 4:
    f2 = int(input('Em quantas vezes deseja parcelar?: '))
    print('Parcelado em {} vezes com juros de 20%, fica {:.2f}R$\mês\n'
          'ao todo ficará {}'.format(f2, t / f2, t))

