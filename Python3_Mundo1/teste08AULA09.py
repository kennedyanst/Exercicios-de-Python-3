#DESAFIO 22
nome = input('Digite seu nome:')
print ('Seu nome em maiusculo é {}:.'.format(nome.upper()))
print ('Seu nome em minusculo é {}'.format(nome.lower()))
espaco = nome.count(' ')
indice = len(nome)
print ('A quantidade de letras no seu nome é de: {}.'.format(indice-espaco))
dividido = nome.split()
print ('A quantidade de letras no seu primeiro nome é de {}.'.format(len(dividido[0])))

#DESAFIO 23
num = input('digite um número de até 4 digitos:')
s = '000' + num
print (f'Unidade: {s[-1]}')
print (f'Dezena: {s[-2]}')
print (f'Centena: {s[-3]}')
print (f'milhar: {s[-4]}')

#DESAFIO 24
nome = input('Digite o nome de uma cidade:')
dividir = nome.split()
print ('Santo' in (dividir[0]))

#DESAFIO 25
nome = input('Digite seu nome completo:')
print ('Silva' in (nome))

#DESAFIO 26
frase = input('Digite uma frase:').upper().strip()
print ('A letra "A" aparece {} vezes nessa frase!'.format(frase.count('A')))
print ('A letra "A" aparece primeiro na posição {}!'.format(frase.find('A')+1))
print ('A letra "A" aparece por ultimo na posição {}!'.format(frase.rfind('A')+1))

#DESAFIO 27
nome = input('Digite seu nome completo:')
fist = nome.split()
last = nome.rsplit(maxsplit=1)
print ('Seu nome completo é: {}.'.format(nome))
print ('Seu primeiro nome é: {}.'. format(fist[0]))
print ('Seu ultimo nome é:{}'.format(last[1]))
