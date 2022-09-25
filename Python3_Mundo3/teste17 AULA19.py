#DESAFIO 90:
Faça um programa que leia 'nome e média'
de um aluno, guardando também a 'situação' em um DICIONÁRIO.
No final, mostre o conteúdo da estrutura na tela.

#RESPOSTA:
situacao = ''
nome = str(input('Qual o nome: '))
media = float(input('Qual a média: '))
if media <= 4.9:
    situacao = 'Reprovado!'
else:
    situacao = 'Aprovado!'
dados = {'Nome': nome, 'Média': media, 'Situação': situacao}
for k, v in dados.items():
    print(f'O(A) {k} é {v}')


#DESAFIO 91:
Crie um programa onde '4 jogadores' joguem um DADO
e tenham resultados ALEATÓRIOS. Guarda esses resultados
em um dicionário. No final, coloque esse dicionário em 'ordem',
sabendo que o VENCEDOR tirou 'maior número' no dado.

#RESOSTA:
lista = []
import random
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1,6),
             'Jogador 2': randint(1,6),
             'Jogador 3': randint(1,6),
             'Jogador 4': randint(1,6)}
ranking = list()
print (f'VALORES SORTEADOS: ')
for k, v in jogadores.items():
    print (f' O {k} tirou: {v} no dado!')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print (f'          RANKING')
print ('-'*30)
for i,v in enumerate(ranking):
    print (f'{i+1}º Lugar: {v[0]} com {v[1]} no DADO')


#DESAFIO 92:
Crie um programa que leia 'nome','ano de nascimento' e
'carteira de trabalho' e cadastre-os (com 'idade') em
uma DICIONÁRIO se por acaso o 'CTPS' for diferente de ZERO,
o dicionário receberá também o 'ano de contratação' e o 'salário'.
Calcule e acrescente, além da 'idade', com quantos anos a pessoa
vai se 'aposentar'.

#RESPOSTA:
nome = str(input('Digite seu nome: '))
nasc = int(input('Digite seu ano de nascimento: '))
idade = (2022 - nasc)
ctps = int(input('Digite o seu CTPS [0 = Não tenho]: '))
if ctps == 0:
    ctps = 'NÃO TEM CARTEIRA DE TRABALHO'
    dados = {'Nome': nome, 'Idade': idade,
             'CTPS': ctps}
    print (dados)
    print (f'Nome: {nome}, Idade: {idade} anos, Não tem CARTEIRA DE TRABALHO.')
else:
    contratacao = int(input('Qual o ano de contratação? '))
    salario = float(input('Qual o salário? '))
    aposentadoria = ((contratacao - nasc) + 35)
    dados = {'Nome': nome, 'Idade(ANOS)': idade,
         'CTPS(CARTEIRA DE TRABALHO)': ctps, 'Contratação(ANO)': contratacao,
         'Salário(R$)': salario, 'Aposentadoria(ANOS)': aposentadoria}
    print (dados)
    for k,v in dados.items():
        print (f'{k} equivale: {v}')
 

#DESAFIO 93:
Crie um programa que gerencie o aproveitamento de um
'jogador de futebol'. O programa vai ler o NOME DO JOGADOR
e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS
feito em 'cada partida'. No final, tudo isso será guardado
em um 'dicionário', incluindo o TOTAL DE GOLS feitos durante
o campeonato.

#RESPOSTA:
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print ('-=' * 30)
print (jogador)
print ('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print ('-=' * 30)
print (f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print (f'    => Na partida {i}, fez {v} gols.')
print (f'Foi um total de {jogador["total"]} gols.')


#DESAFIO 94:
Crie um programa que leia NOME, SEXO e IDADE de 'várias pessoas',
guardando os dados de cada pessoa em um 'dicionário' e todos os
dicionários em uma 'lista'. No final, mostre:

a)Quantas pessoas foram cadastradas.
b)A 'média' de idade do grupo.
c) Uma lista com todas as 'mulheres'.
d) Uma lista com todas as pessoas com 'idade' acima da 'média'.

#RESPOSTA:
acimamed = list()
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print ('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print ('-=' * 30)
print (f'A) A quantidade de pessoas cadastradas foi: {len(galera)}')
media = soma / len(galera)
print (f'B) A média de idade é: {media} anos.')
print (f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print (f'{p["nome"]}, ', end='')
print()
if pessoa['idade'] > media:
    acimamed.append(pessoa['nome'])
elif pessoa['idade'] <= media:
    acimamed = 'NÃO TEM PESSOAS ACIMA DA MÉDIA DE IDADE.'
print (f'D) As pessoas acima da média de idade são: {acimamed}')


#DESAFIO 95:
Aprimore o 'DESAFIO 93' para que ele funcione com VÁRIOS
JOGADORES, incluindo um sistema de visualização de DETALHES
DO APROVEITAMENTO de cada jogador.

#RESPOSTA:
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print ('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print ('-='*30)
print ('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print ()
print ('-'*40)
for k, v in enumerate(time):
    print (f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print ('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print (f'ERRO! Não existe jogador com código {busca}!')
    else:
        print (f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print (f'       No jogo {i+1} fez {g} gols. ')
    print ('-' *40)
print ('<< VOLTE SEMPRE >>')
