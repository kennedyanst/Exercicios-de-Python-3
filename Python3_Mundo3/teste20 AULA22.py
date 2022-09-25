#DESAFIO 107
Crie um módulo chamado 'moeda.py' que tenha as funções
incorporadas AUMENTAR(), DIMINUIR(), DOBRO(), e METADE().
Faça também um programa que 'importe' esse módulo e use
algumas dessas funções.

#RESPOSTA:
#moedas.py
def aumentar(n):
    return n*1.10 #aumento de 10%


def diminuir(n):
    return n*0.90 #diminuição de 10%


def dobro(n):
    return n*2


def metade(n):
    return n/2

#teste.py
import moedas
num = float(input('Digite um valor em R$: '))
print (f'Aumento em 10% de {num} é {moedas.aumentar(num)}')
print (f'A diminuição em 10% de {num} é {moedas.diminuir(num)}')
print (f'O dobro de {num} é {moedas.dobro(num)}')
print (f'A metade de {num} é {moedas.metade(num)}')


#DESAFIO 108
Adapte o código do 'desafio 107', criando uma função
adicional chamada MOEDA() que consiga mostrar os valores
como um valor monetário formatado.

#RESPOSTA:
#moedas.py
def aumentar(n):
    return n*1.10


def diminuir(n):
    return n*0.90


def dobro(n):
    return n*2


def metade(n):
    return n/2


def moeda(n=0):
    return f'R${n:.2f}'.replace('.',',')

#teste.py
import moedas
num = float(input('Digite um valor em R$: '))
print (f'Aumento em 10% de {moedas.moeda(num)} é {moedas.moeda(moedas.aumentar(num))}')
print (f'A diminuição em 10% de {moedas.moeda(num)} é {moedas.moeda(moedas.diminuir(num))}')
print (f'O dobro de {moedas.moeda(num)} é {moedas.moeda(moedas.dobro(num))}')
print (f'A metade de {moedas.moeda(num)} é {moedas.moeda(moedas.metade(num))}')


#DESAFIO 109
Modifique as funções que foram criadas no 'desafio 107'
para que elas aceitem UM PARÂMETRO a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função MOEDA(),
desenvolvida no 'desafio 108'.

#RESPOSTA:
#moedas.py
def aumentar(n):
    return n*1.10


def diminuir(n):
    return n*0.90


def dobro(n):
    return n*2


def metade(n):
    return n/2


def moeda(n=0, formato=False):
    if formato == True:
        return f'R${n:.2f}'.replace('.',',')
    else:
        return f'{n:.2f}'.replace('.',',')

#teste.py
import moedas
num = float(input('Digite um valor em R$: '))
print (f'Aumento em 10% de {moedas.moeda(num,True)} é {moedas.moeda(moedas.aumentar(num),True)}')
print (f'A diminuição em 10% de {moedas.moeda(num,False)} é {moedas.moeda(moedas.diminuir(num),True)}')
print (f'O dobro de {moedas.moeda(num,False)} é {moedas.moeda(moedas.dobro(num),False)}')
print (f'A metade de {moedas.moeda(num,True)} é {moedas.moeda(moedas.metade(num),False)}')

#DESAFIO 110
Acicione ao módulo 'moeda.py' criado nos desafios anteriores,
uma função chamada RESUMO(), que mostre na tela algumas
informações geradas pelas funções que já temos no módulo
criado até aqui.

#RESPOSTA:
#moedas.py
def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço*2
    return res if not formato else moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return  res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print ('-'*30)
    print ('RESUMO DO VALOR'.center(30))
    print ('-'*30)
    print (f'Preço analizado: \t{(moeda(preço))}')
    print (f'Dobro do preço: \t{dobro(preço, True)}')
    print (f'Metade do Preço: \t{metade(preço, True)}')
    print (f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print (f'{taxar}% de diminuição: \t{diminuir(preço, taxar, True)}')
    print('-'*30)

#teste.py
import moedas
num = float(input('Digite um valor em R$: '))
moedas.resumo(num,100,50)


#DESAFIO 111
Crie um 'pacote' chamado 'utilidadesCeV' que tenha dois
MÓDULOS INTERNOS() chamados 'moeda' e 'dado'.
Tranfira todas as funções ultilizadas nos 'desafios 107',
'108' e '109' para o primeiro pacote e mantenha tudo funcionado.

#RESPOSTA:
from utilidadesCeV.moeda1 import moedas

num = float(input('Digite um valor em R$: '))
moedas.resumo(num, 100, 50)


#DESAFIO 112
Dentro do pacote 'utilidadesCeV' que criamos no 'desaio 111', temos
um MÓDULO chamado 'dado'. Crie uma função chamada LEIADINHEIRO() que
seja capaz de funcionar como a função INPUT(), mas com
uma 'validação de dados' para aceitar apenas valores que sejam MONETÁRIOS.

#RESPOSTAS:
FEITO!
