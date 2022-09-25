#DESAFIO 36
casa = int(input('\033[30mDigite o valor da casa:'))
sal = int(input('Digite o valor do seu salario:'))
anos = int(input('Em quantos anos pretende pagar?:\033[m'))
meses = anos*12
prestacao = casa/meses
if prestacao >= 0.30*sal:
    print ('\033[1;41mSeu emprestimo foi negado!!\033[m')
else:
    print ('\033[1;42mSeu emprestimo foi aprovado!\033[m')

#DESAFIO 37
num = int(input('\033[31;40mDigite um número:\033[m '))
bin = bin(num)
octa = oct(num)
hexa = hex(num)
print ("""\033[1;30mESCOLHA A OPÇÃO DE CONVERSÃO QUE VOCÊ QUER:\033[m
 \033[1;97mDigite \033[4m"1"\033[m\033[1;97m para binario!
 \033[1;97mDigite \033[4m"2"\033[m\033[1;97m para hexadecimal!
 \033[1;97mDigite \033[4m"3"\033[m\033[1;97m para octadecimal!\033[m
 """)
num1 = int(input('\033[1;3;4;30mEscolha a conversão:'))
if num1 == 1:
    print ('\033[1;3;40;97mSeu número em binario é:{}!'.format(bin))
elif num1 == 2:
    print ('Seu número em hexadecimal é:{}!'.format(hexa))
elif num1 == 3:
    print ('Seu número em octadecimal é:{}!'.format(octa))
else:
    print ('\033[1;3;9;31mSeu número não é valido, tente novamente!')

#DESAFIO 38
num1 = int(input('\033[36mDigite o primeiro valor:'))
num2 = int(input('\033[35mDigite o segundo valor:'))
if num1 > num2:
    print ('\033[1;36mO primeiro valor: {}, é maior que o segundo valor: {}!'.format(num1,num2))
elif num1 < num2:
    print ('\033[1;35mO segundo valor: {}, é maior que o primeiro valor: {}!'.format(num2,num1))
else:
    print ('\033[1;4;30;107mOs números são iguais!!\033[m')

#DESAFIO 39
data = int(input('\033[30mDigite seu ano de nascimento: \033[m'))
idade = 2022 - data
if idade < 18:
    print ('\033[97mVocê ainda vai se alistar no serviço militar!\033[m')
elif idade == 18:
    print ('\033[97mVocê deve se alistar este ano no serviço militar!\033[m')
    print ('\033[1;44;97mO ALISTAMENTO SERÁ \033[4mDIA 30 DE JUNHO DE 2022!\033[m')
elif idade > 18:
    print ('\033[97mPassou da hora de se alistar no serviço militar!\033[m')
    print ('\033[1;41;97mO ALISTAMENTO MILITAR FOI \033[4m30 DE JUNHO DE 2021!!!!\033[m')

#DESAFIO 40
nota1 = float(input('\033[30;107;1mDIGITE SUA NOTA 1:\033[m '))
nota2 = float(input('\033[97;40;1mDIGITE SUA NOTA 2:\033[m '))
media = (nota1 + nota2)/2
if media < 5.0:
    print ('\033[30mSua média foi: {}. Você foi \033[41;1;4mREPROVADO!!\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print ('\033[30mSua média foi:{}. Você ficou de \033[43;1;4mRECUPERAÇÃO!\033[m'.format(media))
else:
    print ('\033[1;4;97;42mSua média foi:{}. VOCÊ PASSOU!!\033[m'.format(media))

#DESAFIO 41
nome = input('\033[1;30mDigite o nome do atleta:\033[m ')
ano = int(input('\033[3;31mDigite o ano de nascimento do atleta:\033[m '))
idade = 2022 - ano
if idade <= 9:
    print ('\033[97mO(A) atleta \033[4m{}\033[m\033[97m tem {} de idade e a categorida dele é \033[1;40mMIRIM!.\033[m'.format(nome, idade,))
elif idade >= 10 and idade <=14:
    print ('\033[97mO(A) atleta \033[4m{}\033[m\033[97m tem {} de idade e a categorida dele é \033[1;43mINFANTIL!.\033[m'.format(nome, idade,))
elif idade >= 15 and idade <= 19:
    print ('\033[97mO(A) atleta \033[4m{}\033[m\033[97m tem {} de idade e a categorida dele é \033[1;44mJUNIOR!.\033[m'.format(nome, idade,))
elif idade == 20:
    print ('\033[97mO(A) atleta \033[4m{}\033[m\033[97m tem {} de idade e a categorida dele é \033[1;45mSÊNIOR!.\033[m'.format(nome, idade,))
else:
    print('\033[97mO(A) atleta \033[4m{}\033[m\033[97m tem {} de idade e a categorida dele é \033[1;46mMASTER!.\033[m'.format(nome, idade, ))

#DESAFIO 42
a = int(input('\033[30mDIGITE UM \033[1;4mLADO:\033[m '))
b = int(input('\033[97mDIGITE UM \033[1;4mLADO:\033[m '))
c = int(input('\033[36mDIGITE UM \033[1;4mLADO:\033[m '))
formula1 = a + b > c
formula2 = a + c > b
formula3 = c + b > a
if formula3 and formula2 and formula1 and (a == b == c):
    print ('\033[30mÉ um \033[32;1;4mtriângulo!\033[m')
    print ('Seu triângulo é equilatero!')
elif formula3 and formula2 and formula1 and (a == b or a == c or c == b):
    print ('\033[30mÉ um \033[32;1;4mtriângulo!\033[m')
    print ('Seu triângulo é isóceles')
elif formula3 and formula2 and formula1 and (a != b or a != c or c != b):
    print ('\033[30mÉ um \033[32;1;4mtriângulo!\033[m')
    print ('Seu triângulo é escaleno!')
else:
    print ('\033[30mNão é um \033[31;1;4mtriângulo!')

#DESAFIO 43
peso = float(input('\033[1;97mQual o seu peso em KG? \033[m'))
altura = float(input('\033[1;36mQual a sua altura em METROS? \033[m'))
imc = peso / altura**2
if imc < 18.5:
    print ('\033[1;30mSeu imc é:\033[4m{:.2f}\033[m\033[1;30m, você está \033[107mABAIXO DO PESO!\033[m'.format(imc))
elif imc >= 18.5 and imc < 25:
    print ('\033[1;30mSeu imc é:\033[4m{:.2f}\033[m\033[1;30m, você está no \033[44mPESO IDEAL!\033[m'.format(imc))
elif imc >= 25 and imc < 30:
    print ('\033[1;30mSeu imc é:\033[4m{:.2f}\033[m\033[1;30m, você está com \033[42mSOBREPESO!\033[m'.format(imc))
elif imc >= 30 and imc < 40:
    print ('\033[1;30mSeu imc é:\033[4m{:.2f}\033[m\033[1;30m, você está com \033[41mOBESSIDADE!\033[m'.format(imc))
else:
    print ('\033[1;30mSeu imc é:\033[4m{:.2f}\033[m\033[1;30m, você está com \033[4;3;41mOBESSIDADE MÓRBIDA!!!\033[m'.format(imc))

#DESAFIO 44
preco = int(input('\033[1;31mINFORME O VALOR A SER PAGO: \033[m'))
print ('\033[1;32mINFORME A FORMA DE PAGAMENTO: \033[m')
meio = int(input("""\033[97m1- DINHEIRO!
2- CHEQUE!
3- À VISTA NO CARTÃO!
4- 2x NO CARTÃO!
5- 3x OU MAIS NO CARTÃO!
\033[3mQual a sua escolha: \033[m"""))
if meio == 1:
    print ('\033[3;30mVocê escolheu \033[1;4mDINHEIRO.\033[m\033[3;30m O valor a ser pago será:{} reais, com 10% de desconto.\033[m'.format(preco*0.90))
elif meio == 2:
    print ('\033[3;30mVocê escolheu \033[1;4mCHEQUE.\033[m\033[3;30m O valor a ser pago será:{} reais, com 10% de desconto.\033[m'.format(preco*0.90))
elif meio == 3:
    print ('\033[3;30mVocê escolheu \033[1;4;97mÀ VISTA NO CARTÃO.\033[m\033[3;30m O valor a ser pago será:{} reais, com 5% de desconto.\033[m'.format(preco*0.95))
elif meio == 4:
    print ('\033[3;30mVocê escolheu \033[1;4;35m2X NO CARTÃO.\033[m\033[3;30m O valor a ser pago será: 2x de {} reais, sem juros.\033[m'.format(preco/2))
elif meio == 5:
    vezes = int(input('\033[3;36;107mQuantas vezes?: \033[m'))
    print ('\033[3;30mVocê escolheu \033[1;4;36m3X OU MAIS NO CARTÃO.\033[m\033[3;30m O valor a ser pago será: {}x de {} reais, com juros de 20%.\033[m'.format((vezes),(preco*1.20/vezes)))
else:
    print ('\033[1;9;30;41mSUA OPÇÃO NÃO EXISTE!!\033[m')

#DESAFIO 45
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
itens2 = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print ("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
""")
jogador = int(input('Qual a sua jogada? '))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')
print ('-='*11)
print ('Computador jogou:{}.'.format(itens[computador]))
print ('Jogador jogou:{}.'.format(itens2[jogador]))
print ('-='*11)
if computador == 0: # computador jogou PEDRA!
    if jogador == 0:
        print ('EMPATE!')
    elif jogador == 1:
        print ('VOCÊ GANHOU!!')
    elif jogador == 2:
        print ('VOCÊ PERDEU!!')
    else:
        print ('JOGADA INVALIDA!!')
if computador == 1: # computador jogou PAPEL!
    if jogador == 0:
        print ('VOCÊ PERDEU!')
    elif jogador == 1:
        print ('EMPATE!!')
    elif jogador == 2:
        print ('VOCÊ GANHOU!!')
    else:
        print ('JOGADA INVALIDA!!')
if computador == 2: # computador jogou TESOURA!
    if jogador == 0:
        print ('VOÊ GANHOU!')
    elif jogador == 1:
        print ('VOCÊ PERDEU!!')
    elif jogador == 2:
        print ('EMPATE!!')
    else:
        print ('JOGADA INVALIDA!!')
#(NÃO ESTÁ PRONTO!!!!)
