p = float(input('Seu peso (kg): '))
a = float(input('Sua altura (m): '))
imc = p / (a ** 2)
print('O IMC desta pessoa é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <25:
    print('Você está com o peso ideal')
elif 25 < imc <= 30:
    print('Você está no sobrepeso')
elif 30 < imc <= 40:
    print('Você está na Obesidade')
else:
    print('Você está obesidade Mórbita')
