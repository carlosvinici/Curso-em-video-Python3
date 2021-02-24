V = float(input('Qual a velocidade do carro: '))
if V > 80:
    print('Você excedeu a velocidade permitida! de 80km/h')
    print('Você será multado em {:.2f}$'.format((V - 80) * 7))
    print('Dirija com mais cuidado! Respeite a vida!S2')
else:
    print('Tenha um Bom dia! Dirija com segurança!')
