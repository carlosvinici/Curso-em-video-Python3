print('==' * 5, 'Cadastro de Pessoas', '==' * 5)
resposta = ' '
maisde18 = 0
Fmenosde20 = 0
totdehomens = 0
totpessoas = 0
while resposta not in 'Nn':
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Masculino ou Feminino [M / F]: ')).upper().strip()[0]
    resposta = str(input('Quer continuar?[S/N] '))
    totpessoas += 1
    if sexo == 'M':
        totdehomens += 1
    if sexo == 'Ff' and idade < 20:
        Fmenosde20 += 1
    if idade > 18:
        maisde18 += 1
print(f'Total de pessoas cadastradas: {totpessoas}')
print(f'Total de Homens cadastrados: {totdehomens}')
print(f'Total de mulheres com menos de 20 anos: {Fmenosde20}')
print(f'Total de Pessoas com mais de 18 anos: {maisde18}')

