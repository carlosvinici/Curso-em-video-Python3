soma = cont = 0
while True:
    numero = int(input('Digite um numero [digite 999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} numeros e a soma entre eles é {soma}. ')
