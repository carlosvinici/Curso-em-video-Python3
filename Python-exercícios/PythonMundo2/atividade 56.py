sexo = str(input('Qual sexo? M/F: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('dados invalidos porfavor digite novamente:  ')).upper().strip()[0]
print('sexo {} resgistrado'.format(sexo))
print('fim')