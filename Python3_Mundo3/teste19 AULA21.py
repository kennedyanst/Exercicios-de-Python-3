#DESAFIO 101
Crie um programa que tenha uma FUNÇÃO chamada 'voto()' que
vai receber como PARÂMETRO o 'ano de nascimento' de uma pessoa,
RETORNANDO um valor 'literal' indicando se uma pessoa tem voto 'NEGADO',
'OPCIONAL' ou 'OBRIGÁTORIO' nas eleições.

#RESPOSTA:
def voto(ano):
    idade = (2022 - ano)
    print (f'Sua idade é: {idade} anos.')

    if idade < 16:
        return print('\033[30;41;1mSeu voto é \033[4mNEGADO!\033[m')
    elif idade == 16 or ano == 17:
        return print('\033[30;44mSeu voto é \033[1;4mOPCIONAL\033[m')
    elif idade >= 18:
        return print('\033[97;42mSeu voto é \033[1;4mOBRIGATORIO!\033[m')


ano = int(input('\033[1;97mDigite seu ano de nascimento: '))
voto(ano)


#DESAFIO 102
Crie um programa que tenha uma FUNÇÃO 'fatorial()' que receba
dois parâmetros: o primeiro que indique o NÚMERO a calcular e o
outro chamado SHOW, que será um valor 'lógico'(OPCIONAL) indicando
se será mostrado ou não na tela o processo de calculo do fatorial.

#RESPOSTA:
def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print (' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(10, show = True))


#DESAFIO 103
Faça um programa que tenha um FUNÇÃO chamada 'ficha()', que
receba dois PARÂMETROS OPCIONAIS: o 'nome' de um jogador e quantos 'gols'
ele marcou.
O prorama deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum
dado não tenha sido informado corretamente.

#RESPOSTA:
def ficha(jog='<desconhecido>', gol=0):
    print (f'O jogador {jog} fez {gol} gols(s) no campeonato.')

n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
    

#DESAFIO 104
Crie um programa que tenha a FUNÇÃO 'leiaInt()', que vai funcionar de
forma semelhante à função 'input()' do Python, só que fazendo a
'validação' para aceitar apenas um valor numérico.
Ex:
    n = leiaInt('Digite um n')

#RESPOSTA:
def leaiInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print ('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n= leaiInt('\033[30;1mDigite um número: \033[m')
print(f'\033[30;42mVocê acabou de digitar o número: {n}')


#DESAFIO 105
Faça um programa que tenha uma FUNÇÃO 'notas()' que pode receber
várias notas de alunos e vai retornando um DICIONÁRIO com as
seguites informações:
    - Quantidade de notas.
    - A maior nota.
    - A menor nota.
    - A média da turma.
    - A situação (Opcional)
Adicione também as DOCSTRINGS da função.

#RESPOSTA:
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'BOA'
        elif r['media'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)

#DESAFIO 106:
Faça um 'mini-sistema' que utilize o INTERACTIVE HELP do 'Python'.
O usuário vai digitar o COMANDO e o 'manual' vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use CORES!

#RESPOSTA:
from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[97;40m'
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6],end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' *tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)
