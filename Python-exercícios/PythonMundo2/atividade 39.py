from datetime import date
ano = int(input('Qual o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu no ano de {} tem {} anos.'.format(ano, idade))
if idade == 18:
    print('Você deve se alistar imediatamente ou pagara taxas')
elif idade < 18:
    print('Ainda faltam {} anos para você poder se alistar.'.format(18 - idade))
else:
    print('Você tem {} anos, você está atrasado {} anos, será taxado.'.format(idade, idade - 18))
