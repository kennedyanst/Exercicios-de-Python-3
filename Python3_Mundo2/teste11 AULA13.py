#DESAFIO 46
import time
from time import sleep
for c in range(10,0,-1):
    print ('\033[1;30m',c)
    time.sleep(1)
print ('\033[107;4;3mFeliz ano novo!!\U0001F923\033[m')

#DESAFIO 47
print ('Os números pares de 0 a 50 são:')
for c in range(2,50+2,2):
    print ('\033[97;3;1;4m',(c))
print ('\033[7mFIM!!\033[m')

#DESAFIO 48
soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 ==0:
        soma = soma +c
        cont = cont +1
print ('\033[1;97mA soma entre os \033[3;4;30m{}\033[m\033[1;97m elementos, ficará: \033[40m{}\033[m'.format(cont,soma))

#DESAFIO 49
print ('\033[1;4;9;30m-=\033[m'*9)
num = int(input('\033[97;3;1mDIGITE UM NÚMERO: \033[m'))
print ('\033[1;36;40mA TABUADA DE \033[4m{}\033[m\033[1;36;40m E:\033[m'.format(num))
for c in range(1,21):
    print ('\033[30m{} x \033[36m{} = \033[97m{}'.format(c,num,c*num))
print ('\033[1;4;9;30m-=\033[m'*9)

#DESAFIO 50
s = 0
for c in range(0,6):
  n = int(input('Digite um número: '))
  if n%2 == 0:
    s+=n
print(s)

#DESAFIO 51
num = int(input('\033[30;1;3mDigite o primeiro termo da sua PA: '))
razao = int(input('Digite a razão da sua PA: '))
termo = num + (11-1)* razao
for c in range(num,termo,razao):
    print ('\033[4;34m{}\033[m'.format(c), end='\033[30m -\033[m ')
print ('\033[1;97mACABOU!!')

#DESAFIO 52
n = int(input("Verificar numeros primos ate: "))
mult=0
for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1
if(mult==0):
    print("É primo")
else:
    print('Tem {} múltiplos acima de 2 e abaixo de {}'.format(mult,n))

#DESAFIO 53
frase = str(input('\033[36mDigite uma frase para saber se é um \033[1;4mPALINDROMO:\033[m '))
espaco = ' '
for x in range(len(espaco)):
    frase = frase.replace(espaco[x],'')
if str(frase) == str(frase)[::-1]:
    print ('\033[3;1;32mÉ um \033[30;4;42mPALINDROMO\033[m')
else:
    print ('\033[1;3;30;41mNÃO É um PALINDROMO\033[m')

#DESAFIO 54
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,7):
    ano = int(input('\033[3;30mO ano da \033[4m{}ª\033[m\033[3;30m pessoa é: \033[m'.format(pess)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print ('\033[1;97mAo todo, tivemos um total de {} pessoas maiores de 18 anos.'.format(totmaior))
print ('Tambem tivemos um total de {} menores de 18 anos.'.format(totmenor))

#DESAFIO 55
lista = []
for pess in range(1,6):
    peso = float(input('\033[1;3;97mDIGITE O PESSO DA \033[1;3;4;30m{}ª\033[m\033[1;3;97m PESSOA!\033[m'.format(pess)))
    lista+=[peso]
print ('\033[1;36mO maior peso é:\033[9m{}!\033[m'.format(max(lista)))
print ('\033[1;31mO menor peso é:\033[9m{}!\033[m'.format(min(lista)))

#DESAFIO 56
somaidade = 0
mediaidade = 0
maioridadehomem = 0
homemvelho = ''
totmulher20 = 0
for pess in range(1,5):
    print ('\033[1;30m====== \033[m\033[3;36mDADOS DA {}ª PESSOA!.\033[m\033[1;30m======'.format(pess))
    nome = str(input('\033[1;4;97mNome da pessoa:\033[m ')).strip()
    idade = int(input('\033[1;3;41;30mIdade da pessoa:\033[m '))
    sexo = str(input('\033[9;35mDigite o sexo [M/F] da pessoa: \033[m')).strip()
    somaidade += idade
    if pess == 1 and sexo in 'Mm':
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print ('\033[1;32mA média da idade entre os 4 é: \033[30;41m{}.\033[m'.format(mediaidade))
print ('\033[1;32mO homem mais velho tem: \033[30m{}\033[m\033[1;32m e se chama: \033[1;97m{}.\033[m'.format(maioridadehomem, homemvelho))
print ('\033[1;32mExistem \033[35m{} mulher\033[m\033[1;32m com menos de 20 anos!\033[m'.format(totmulher20))
