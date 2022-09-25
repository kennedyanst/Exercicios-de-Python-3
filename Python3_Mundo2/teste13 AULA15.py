#DESAFIO 66
n = s = c = 0
while True:
    n = int(input('\033[1;30mDigite um número [DIGITE 999 PARA PARAR!]: '))
    if n == 999:
        break
    s += n
    c += 1
print (f'\033[3;107m{c} números foram contados e a soma é {s: ^20}\033[m')

#DESAFIO 67
n = 0
while True:
    print('\033[1;97m=-=\033[m' * 10)
    n = int(input('\033[1;36mDigite UM NÚMERO para saber A TABUADA:\033[m '))
    print('\033[1;97m=-=\033[m' * 10)
    print(f'\033[1;4;36mTABUADA DO {n}\033[m')
    print('\033[1;30m=-=\033[m' * 10)
    if n <= 0:
        break
    for c in range(1,11):
        print (f'\033[1;36m{c} \033[30mx \033[97m{n} \033[30m= \033[35m{c*n}')
print ('\033[1;4;9;97mFIMMM!!!')

#DESAFIO 68
import random
from random import randint
v = 0
while True:
    jogador = int(input('\033[1;30mDigite um número: \033[m'))
    computador = random.randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[1;97mVOCÊ QUER PAR OU ÍMPAR? \033[4m[P/I]:\033[m ')).strip().upper()[0]
    print (f'\033[3;36mVocê jogou {jogador} e o computador jogou {computador}, \033[4mo total deu {total}.\033[m ',end='')
    print (f'\033[1;30mDEU PAR!\033[m' if total%2 == 0 else 'DEU ÍMPAR!\033[m')
    if tipo == 'P':
        if total %2 == 0:
            print ('\033[44;97mVOCÊ GANHOU!!\033[m')
            v += 1
        else:
            print ('\033[30;41mVocê perdeu!!\033[m')
            break
    elif tipo == 'I':
        if total %2 == 1:
            print ('\033[44;97mVOCÊ GANHOU!!\033[m')
            v +=1
        else:
            print ('\033[30;41mVocê perdeu!!!!\033[m')
            break
    print ('\033[30;107mVamos jogar NOVAMENTE!\033[m')
print (f'\033[1;31mGAME OVER!!\033[m \033[1;97mVocê venceu \033[4m{v} vezes!')

#DESAFIO 69
tot18 = tothom = tot20mu = 0
while True:
    print('\033[1;9;31m-=\033[m'*10)
    print('\033[1;3;30;107mCADASTRO DE PESSOAS!\033[m')
    print('\033[1;9;31m-=\033[m' * 10)
    idade = int(input('\033[1;4;30mDigite a idade da pessoa:\033[m '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('\033[1;4;36mDigite o sexo[M/F]:\033[m ')).strip().upper()[0]
    if idade >= 18:
        tot18 =+1
    if sexo == 'M':
        tothom += 1
    if idade < 20 and sexo == 'F':
        tot20mu +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;32mQUER CONTINUAR?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
            break
print ('\033[1;9;97m>-\033[m'*20)
print (f'\033[1;3;97mO Total de pessoas com mais de 18 anos é:{tot18}')
print (f'O total de homens é:{tothom}')
print (f'O total de mulheres com menos de 20 anos é:{tot20mu}')

#DESAFIO 70
import time
from time import sleep
total = totmil = cont = menor = 0
barato =''
while True:
    print ('\033[1;9;30m=\033[m'*15)
    print ('\033[1;4;36mLOJAS TRIBO\033[m')
    print('\033[1;9;30m=\033[m' * 15)
    produto = str(input('\033[1;32;107mDigite o NOME do PRODUTO:\033[m '))
    preco = int(input('\033[1;35;40mDigite o PREÇO:\033[m '))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    if preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[1;31mQuer continuar?[S/N]: \033[m')).strip().upper()[0]
    if resp == 'N':
            break
print ('\033[1;4;9;97m>\033[m'*20)
print ('\033[30mFIM DO PROGRAMA...\033[m')
time.sleep(1)
print (f'\033[97mO valor total deu: R$ {total}.')
time.sleep(1)
print (f'O produto mais barato é:{barato} e custa R$ {menor}.')
time.sleep(1)
print (f'{totmil} produtos custam mais de R$ 1000.')

#DESAFIO 71
print ('\033[30m>-<\033[m'*5)
print ('\033[97mBANCO PC\033[m')
print ('\033[30m>-<\033[m'*5)
valor = int(input('\033[1;36mDigite o seu "SAQUE" R$:\033[m '))
cont50 = cont20 = cont10 = cont1 = 0
while True:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20 and valor < 50:
        valor -= 20
        cont20 += 1
    elif valor >= 10 and valor < 20:
        valor -= 10
        cont10 += 1
    elif valor >= 1 and valor < 20:
        valor -= 1
        cont1 += 1
    if valor < 1:
        break
print(f'\033[1;31mTotal de {cont50} cédulas de R$50' if cont50 > 0 else '')
print(f'Total de {cont20} cédulas de R$20' if cont20 > 0 else '')
print(f'Total de {cont10} cédulas de R$10'if cont10 > 0 else '')
print(f'Total de {cont1} cédulas de R$1'if cont1 > 0 else '')
