#DESAFIO 72
num = int(input('\033[30mDigite um número entre [0 a 20]:\033[m '))
while num > 20 or num <0:
    num = int(input('\033[1;30;41mDIGITE UM NÚMERO DE 0 A 20, \033[4mFILHO DA PUTA!:\033[m '))
ext = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print (f'\033[1;3;97mO numero {num} por extenso é: \033[4m{ext[num]}')

#DESAFIO 73
primeiros = ('Corinthians.', 'Bragantino.', 'ALT MG', 'Santos', 'Coritiba') # 5 primeiros
ultimos = ('Atletico GO', 'Goiás', 'Juventude', 'Fortaleza') #4 ultimos
ordem = ('Corinthians.', 'Bragantino.', 'ALT MG', 'Santos', 'Coritiba', 'Cuiabá', 'Inter', 'Avai', 'America MG', 'Palmeiras', 'Flamengo', 'Botafogo', 'São Paulo', 'Fluminense', 'Ceará', 'Athletico PR', 'Atletico GO', 'Goiás', 'Juventude', 'Fortaleza')
opcao = 0
while opcao !=5:
    print("""\033[1;30m============\033[97mMENU\033[30m============\033[m
        \033[1;31mAPERTE [1] para ver os 5 PRIMEIROS.\033[m
        \033[1;32mAPERTE [2] para ver os 4 ULTIMOS.\033[m
        \033[1;33mAPERTE [3] para ver todos os times em ORDEM ALFABETICA.\033[m
        \033[1;34mAPERTE [4] para saber em qual posição está a CHAPECOENSE.\033[m
        \033[1;35mAPERTE [5] para SAIR.\033[m""")
    opcao = int(input('\033[1;36mDigite sua OPÇÃO:\033[m '))
    while opcao not in (1, 2, 3, 4, 5):
        opcao = int(input('\033[1;4;30;41mDIGITE UMA OPÇÃO VÁLIDA:\033[m '))
    if opcao == 1:
        print(f'\033[1:30m{primeiros}')
    elif opcao == 2:
        print(f'\033[1;9;31m{ultimos}')
    elif opcao == 3:
        print(sorted(ordem))
    elif opcao == 4:
        print('\033[107;32mA Chapecoense está em 4º LUGAR no \033[4mBrasileirão Serie B\033[m')
    elif opcao == 5:
        break
print('FIM DO PROGRAMA!!')

#DESAFIO 74
import random
from random import randint
nums = (randint(0,6), randint(0,6), randint(0,6), randint(0,6), randint(0,6), randint(0,6), )
print ('\033[1;97m=-\033[m'*10)
print ('\033[1;35mGERADOR DE NÚMEROS.\033[m')
print ('\033[1;97m=-\033[m'*10)
print (f'\033[3;30mOs números gerados foram: \033[1;4m{nums}\033[m')
print (f'\033[1;36;40mO maior é: {max(nums)}\033[m')
print (f'\033[1;36;40mO menor é: {min(nums)}\033[m')

#DESAFIO 75
num = (int(input('Digite um número: ')),int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número:')))
print(f'\033[1;31mOs números digitados foram:{num}\033[m')
print(f'\033[1;3;36mO número 9 foi digitado {num.count(9)} vezes\033[m')
print(f'\033[1;35mO número 3 foi digitado na {num.index(3)+1}ª posição\033[m')
for n in num:
    if n % 2 == 0:
        (print(f'\033[30mvalores pares: {n}\033[m'))

#DESAFIO 76
mangas = ('Naruto', 20.30,
          'Kimetsu no Yaiba', 19.50,
          'Dragon Ball', 22.00,
          'Hunter x Hunter', 21.00,
          'Death Note', 20.30,
          'Naruto Shippuden', 20,
          'Shingeki no Kyojin', 21.20,
          'One Punch Man', 20,
          'Black Clover', 19.50,
          'Dororo', 20)
print ('\033[40;1;9;36m-\033[m'*40)
print (f'\033[1;46;30m{"LOJA DE MANGÁS":^40}\033[m')
print ('\033[40;1;9;36m-\033[m'*40)
for list in range(0,len(mangas)):
    if list % 2 == 0:
        print (f'\033[1;4;97m{mangas[list]:.<30}\033[m',end='')
    else:
        print (f'\033[1;3;32mR$:{mangas[list]:>6.2f}')
