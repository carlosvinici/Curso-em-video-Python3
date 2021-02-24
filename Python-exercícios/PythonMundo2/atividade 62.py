print('==='*12)
numeros = cont = soma = 0
numeros = int(input('Digite um numero [999 para encerrar]: '))
while numeros != 999:
    cont += 1
    soma += numeros
    numeros = int(input('Digite um numero [999 para encerrar]: '))
print('{} numeros digitados,{} a soma dos numeros digitados. '.format(cont, soma))
print('==='*12)