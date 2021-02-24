from datetime import date
print('Classificador de atleta p/ IDADE ({})'.format(date.today().year))
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você nasceu em {} portanto sua idade é {} anos:'.format(nasc, idade))
if idade <= 9:
    print('Você é Mirim')
elif 9 < idade <= 14:
    print('Você é Infatil')
elif 14 < idade <= 19:
    print('Você é Junior')
elif 19 < idade <= 25:
    print('Você é Senior')
else:
    print('Você é Master')

