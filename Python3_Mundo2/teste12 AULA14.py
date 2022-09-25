#DESAFIO 57
sexo = str(input('\033[1;97mDIGITE SEU SEXO \033[4m[M/F]\033[m: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('\033[1;31mDADOS INVÁLIDOS\033[m\033[1;97m, Digite novamente seu sexo [M/F]: ')).strip().upper()[0]
print ('\033[1;30mSexo {} registrado com \033[107;32mSUCESSO!!\033[m'.format(sexo))

#DESAFIO 58
import random
count = 0
print ('\033[30mQual número \033[1;4mentre 0 e 10\033[m\033[30m eu pensei?\033[m')
n1 = random.randint(0,10)
resp = int(input('\033[97mDigite a \033[3;9mresposta:\033[m '))
if resp == n1:
    print ('Você acertou de PRIMEIRA!!!')
else:
    while resp != n1:
        count = count + 1
        resp = int(input('\033[1;31mVocê errou, \033[1;30;4mTENTE NOVAMENTE!!: \033[m'))
        if resp == n1:
            print ('\033[1;3;4;32mVocê acertou! E precisou de {} chance(s) para vencer!\033[m'.format(count))

#DESAFIO 59
from time import sleep
num1 = int(input('\033[36mDigite um número: '))
num2 = int(input('Digite outro número: \033[m'))
opcao = 0
while opcao != 5:
    print ("""\033[1;30m==============\033[97mMENU\033[30m==============\033[m
    \033[3;97mDIGITE \033[1;31m[1]\033[m\033[3;97m: se quiser \033[1;4mSOMAR!\033[m
    \033[3;97mDIGITE \033[1;32m[2]\033[m\033[3;97m: se quiser \033[1;4mMULTIPLICAR!\033[m 
    \033[3;97mDIGITE \033[1;33m[3]\033[m\033[3;97m: se quiser \033[1;4mO MAIOR\033[m
    \033[3;97mDIGITE \033[1;34m[4]\033[m\033[3;97m: se quiser \033[1;4mNOVOS NÚMEROS!\033[m
    \033[3;97mDIGITE \033[1;35m[5]\033[m\033[3;97m: se quiser \033[1;4mSAIR!!\033[m""")
    opcao = int(input('\033[1;9;30m>>>>>>>>>>>\033[m\033[97m Qual a opção desejada?:\033[m '))
    if opcao == 1:
        print ('\033[1;107;31mA soma dos números {} e {} é: {}!\033[m'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print ('\033[1;107;32mA multiplicação dos números {} e {} é: {}!\033[m'.format (num1, num2, num1*num2))
    elif opcao == 3:
        if num2 > num1:
            print ('\033[1;107;33m{} é maior que {}!\033[m'.format(num2, num1))
        elif num1 > num2:
            print ('\033[1;107;33m{} é maior que {}!\033[m'.format (num1, num2))
        else:
            print ('\033[1;97;43mOS NÚMEROS SÃO IGUAIS!\033[m')
    elif opcao == 4:
        num1 = int(input('\033[1;107;34mDigite NOVAMENTE o primeiro número:\033[m '))
        num2 = int(input('\033[1;107;34mDigite NOVAMENTE o segundo número:\033[m '))
    elif opcao == 5:
        print ('\033[1;35mFinalizando....\033[m')
    else:
        print ('\033[41;30;1mOPÇÃO INVALIDA, TENTE NOVAMENTE!!\033[m')
    print ('\033[1;30m=-='*10)
    sleep(2)
print ('\033[1;97;40mFIM DO PROGRAMA, volte sempre!\033[m')

#DESAFIO 60
n = int(input('\033[97mDigite um número para saber o seu \033[1;4mFATORIAL(!):\033[m '))
c = n
f = 1
print ('\033[1;30mCalculando o {}! =\033[m'.format(n), end='')
while c > 0:
    print (' \033[31m{}\033[m '.format(c), end='')
    print ('\033[36mX\033[m' if c > 1 else '=', end='')
    f *= c
    c-=1
print (' \033[1;4;107;30m{}.\033[m'.format(f))

#DESAFIO 61
print ('\033[1;9;97m=-=\033[m'*7)
n = int(input('\033[30mDigite o \033[1;4m1º TERMO:\033[m '))
razao = int(input('\033[35mDigite a \033[1;4mrazão:\033[m '))
print ('\033[1;9;97m=-=\033[m'*7)
termo = n
cont = 1
while cont <= 10:
    print ('\033[1;30m{} \033[97m> \033[m'.format(termo), end='')
    termo += razao
    cont += 1
print ('\033[97mFIMMMM!!!')

#DESAFIO 62
import time
from time import sleep
print ('\033[1;9;97m=-=\033[m'*7)
n = int(input('\033[30mDigite o \033[1;4m1º TERMO:\033[m '))
razao = int(input('\033[35mDigite a \033[1;4mrazão:\033[m '))
print ('\033[1;9;97m=-=\033[m'*7)
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print ('\033[1;30m{} \033[97m> \033[m'.format(termo), end='')
        termo += razao
        cont += 1
    print ('\033[97mPAUSA!')
    mais = int(input('Quantos termos deseja mostrar à mais?: '))
time.sleep(1)
print ('Fim da progressão...')
time.sleep(1)
print ('{} termos foram mostrados!'.format(total))

#DESAFIO 63
print ('\033[1;9;97m-\033[m'*30)
print ('\033[1;3;40;97mSEQUÊNCIA DE FIBONACCI!\033[m')
print ('\033[1;9;97m-\033[m'*30)
n = int(input('\033[1;34mDigite quantos números quer na sua sequência: '))
print ('\033[1;4;30m~~\033[m'*23)
t1 = 0
t2 = 1
print ('\033[1;36m{} \033[97m> \033[36m{}\033[m'.format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print (' \033[97m> \033[36m{}\033[m'.format(t3), end='')
    t1 = t2
    t2 = t3
    count+=1
print (' \033[1;30m> FIM!!')

#DESAFIO 64
num = cont = soma = 0
print ('\033[1;4;30m^^\033[m'*10)
num = int(input('\033[1;36mDIGITE UM NÚMERO: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('\033[35mDigite um número [999 PARA PARAR!!]: '))
print ('\033[1;4;30m^^\033[m'*10)
print ('\033[1;97mVocê digitou \033[4m{} números\033[m\033[1;97m e a \033[4msoma deles é:{}!'.format(cont, soma))

#DESAFIO 65
num = maior = menor = soma = media = cont = 0
print ('\033[1;4;30m^^\033[m'*10)
num = int(input('\033[1;36mDIGITE UM NÚMERO: '))
while num != 999:
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    num = int(input('\033[35mDigite um número [999 PARA PARAR!!]: '))
print ('\033[1;4;30m^^\033[m'*10)
print ('\033[1;97mVocê digitou \033[4m{} números\033[m\033[1;97m e a \033[4mmedia entre eles é:{}!'.format(cont, media))
print ('O MAIOR COMPUTADO foi {}, e o MENOR COMPUTADO foi {}.'.format(maior, menor))
