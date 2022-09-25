#DESAFIO 84:
Faça um programa que leia 'nome e peso' de 'várias pessoas',
guardando tudo em uma LISTA. No final, mostra:
    a)'Quantas' pessoas foram cadastradas.
    b) Uma listagem com as pessoas mais 'pesadas'.
    c) Uma listagem com as pessoas mais 'leves'.

#RESPOSTA!!!
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('\033[30;1mNome:\033[m ')))
    temp.append(float(input('\033[3;97mPeso:\033[m ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('\033[4;36mQuer continuar[S/N]:\033[m '))
    if resp in 'Nn':
        break
print (f'\033[1;32mA quantidade de pessoas cadastradas:\033[m {len(princ)}')
print (f'\033[1;33mO maior peso foi: {mai}Kg. Peso de \033[m', end='')
for p in princ:
    if p[1] == mai:
        print(f'\033[30m[{p[0]}]\033[m', end='')
print()
print (f'\033[1;34mO menor peso foi: {men}Kg. Peso de \033[m', end='')
for p in princ:
    if p[1] == men:
        print(f'\033[30m[{p[0]}]\033[m', end='')
print()


#DESAFIO 85:
Crie um programa onde o usuário possa digitar
'sete valores numéricos' e cadastre-os em uma LISTA ÚNICA que
mantenha separados os valores 'pares' e 'ímpares'.
No final, mostre os valores pares e ímpares em ordem 'crescente'.

#RESPOSTA:
num = [[], []]
valor = 0
for c in range(0,7):
    valor = int(input(f'\033[1;97mDigite o \033[30m{c+1}º\033[m\033[1;97m valor:\033[m '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print (f'\033[1;97mOs números \033[4mpares\033[m\033[1;97m são: {num[0]}\033[m')
print (f'\033[1;30mOs números \033[4mímpares\033[m\033[1;30m são: {num[1]}')


#DESAFIO 86:
Crie um programa que crie uma 'matriz' de DIMENSÃO 3X3 e
preencha com valores lidos pelo teclado.
No final, mostre a 'matriz' na tela com a formatação correta.

#RESPOSTA:
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print ('-='*10)
print (f'GERADOR DE MATRIZ')
print ('-='*10)
for l in range(0,3):
    for c in range(0,3):
        print (f'[{matriz[l][c]:^5}]', end='')
    print()


#DESAFIO 87:
Aprimode o 'desafio anterior', mostrando no final:
    a) A 'soma' de todos os VALORES PARES digitados.
    b) A 'soma' dos valores da TERCEIRA COLUNA
    c) O 'maior' valor da SEGUNDA LINHA.

#RESPOSTA:
matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mai = scol = 0
for l in range (0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print ('-='*10)
print (f'GERADOR DE MATRIZ')
print ('-='*10)
for l in range(0,3):
    for c in range(0,3):
        print (f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] %2 == 0:
            spar+= matriz[l][c]

    print()
print ('-'*20)
print (f'a soma dos pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print (f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print (f'O maior valor da segunda linha é {mai}.')
print ('-='*10)


#DESAFIO 88:
Faça um programa que ajude um jogador da 'MEGA SENA' a criar
PALPITES. O programa vai perguntar QUANTOS JOGOS serão
gerados e vai sortear '6 números' ENTRE 1 E 60 para cada
jogo, cadastrando tudo em uma 'lista composta'.

#RESPOSTA:
from random import randint
from time import sleep
cont = 0
lista = list()
jogos = list()
print ('     \033[1;4;40;35mJOGA NA MEGA SENA!\033[m     ')
print ('\033[1;9;30m-\033[m'*30)
quant = int(input('\033[1;97mQuantos jogos serão sorteados?\033[m '))
tot=1
while tot<= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
            if cont >=6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print ('\033[1;30m-='*3, f'\033[36mSORTEANDO {quant} JOGOS\033[m', '\033[1;30m-=\033[m' * 3)
for i, l in enumerate(jogos):
    print (f'\033[1;31mJogo {i+1}: {l}\033[m')
    sleep(1)
print ('\033[1;30m-=' * 5, '< CONFIA NO PAE! >', '-=' * 5 )


#DESAFIO 89:
Crie um programa que leia 'nome' e 'duas notas' de vários
alnos e guarde tudo em uma LISTA COMPOSTA. No final, mostre
um 'boletim' contendo a 'média' de cada um e permita que o usuário
possa mostrar as NOTAS de cada aluno individualmente.

#RESPOSTA:
ficha = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2 :'))
    media = ((nota1 + nota2) / 2)
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

print (f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print ('-'* 26)
for i, a in enumerate(ficha):
    print (f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print ('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print ('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print (f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print ('<<<< VOLTE SEMPRE >>>>')
