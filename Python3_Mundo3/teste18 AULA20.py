#DESAFIO 96
Faça um programa que tenha uma FUNÇÃO chamada 'área()',
que receba as dimenções de um terreno retangular ('largura' e 'comprimento')
e mostre a ÁREA DO TERRENO.

#Resposta:
def area(l,c):
    s = l*c
    print (f'A área de um terreno {l}X{c} é de {s}m².')


l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
area(l,c)


#DESAFIO 97
Faça um programa que tenha uma FUNÇÃO chamada 'escreva()',
que receba um texto qualquer como PARÂMETRO e mostre uma
mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!')

Saída:
~~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~~

#Respota:
#def escreva(msg):
    tam = len(msg)
    print ('~'*tam)
    print (msg)
    print ('~'*tam)


escreva('Olá, Mundo!')
escreva('Python TEXT!!!!')
escreva('COMO ANDA AS COISAS???')
escreva('Bye')


#DESAFIO 98
Faça um programa que tenha uma FUNÇÃO chamada 'contador()',
que receba três PARÂMETROS: 'início', 'fim' e 'passo' e realize a contagem.

Seu programa tem que realizar TRÊS CONTAGENS através da função criada:
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem PERSONALIZADA.

#RESPOSTA:
from time import sleep
def contador(i,f,p):
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    print ('-='*20)
    print (f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)

    if i < f:
        cont = i
        while cont <=f:
            print (f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print ('FIM!')
    else:
        cont = i
        while cont >= f:
            print (f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print ('FIM!')

#prog principal
contador(1,10,1)
contador(10,0,2)
print ('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini,fim,pas)


#DESAFIO 99
Faça um programa que tenha uma FUNÇÃO chamada 'maior()', que
receba vários parâmetros com valores inteiros. Seu programa tem
que analisar todos os valores e dizer qual delas é o MAIOR.

#RESPOSTA:
from time import sleep
def maior(*num):
    cont = maior = 0
    print ('-='*15)
    print(f'Os números recebidos foram:')
    sleep(1)
    for valor in num:
        print (f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print (f'Foram informados {cont} valores ao todo!')
    print (f' O maior valor foi {maior}.')


maior(1,4,3,2,5,2,1,4,10,76)
maior (10,33,45,100,2909)
maior(121,22,00,1,2,3,4,900)
maior(122,11,90,43,100023)


#DESAFIO 100
Faça um programa que tenha uma LISTA chamada 'números' e
duas FUNÇÕES chamadas 'sorteio()' e 'somaPar()'. A primeira
função vai sortear 5 NÚMEROS e vai colocá-los dentro da lista
e a segunda função vai mostrar a SOMA entre todos os valores
'PARES' sorteados pela função anterior. 

#RESPOSTA:
from time import sleep
from random import randint
def sorteio(lista):
    print (f'Sorteando 5 valores da lista: ', end='')
    for c in range(0,5):
        n = randint(1,50)
        lista.append(n)
        print (f'{n} ', end='')
        sleep(0.5)
    print ('PRONTO!!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print (f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)
