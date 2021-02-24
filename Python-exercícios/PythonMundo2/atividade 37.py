nu = int(input('Digite um número: '))
print('''\033[0;34mEscolha uma opção para a conversão;
[1] Para Números Binários
[2] Para Números Hexadecimais
[3] Para Números Octal''')
op = int(input('\033[1mSua opção: '))
if op == 1:
    print('\033[1;31m{} convertido em número Binário é {}'.format(nu, bin(nu)[2:]))
elif op == 2:
    print('\033[1;32m{} convertido em Hexadecimal é {}'.format(nu, hex(nu)[2:]))
elif op == 3:
    print('\033[1;35m{} Convertido em Octal é {}'.format(nu, oct(nu)[2:]))
print('\033[1;32mObrigado!!!')




