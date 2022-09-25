#DESAFIO 113
Reescreva a função LEIAINT() que fizemos no "desafio 104", incluindo
agora a possibidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função LEIAFLOAT() com a mesma funcionalidade.
#RESPOSTA:
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ("\033[30;41mERRO! Por favor, digite um número válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print ('\033[31;40mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print ("ERRO! Por favor, digite um número válido.")
            continue
        except (KeyboardInterrupt):
            print ('\033[31mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n


n1 = leiaInt("Digite um número INTEIRO: ")
n2 = leiaFloat("Digite um número REAL: ")
print (f"\033[97;40mOs números digitados foram: {n1} e {n2}. ")


#DESAFIO 114
Crie um código em PYTHON que testa se o site "Pudim" está
acessível pelo computador usado.
#RESPOSTA:
from selenium import webdriver
import urllib
import urllib.request


#navegador = webdriver.Chrome()
try:
    #navegador.get("http://pudim.com.br/")
    #print("\033[41mCONSEGUI!!!\033[m")
    urllib.request.urlopen("http://pudim.com.br/")
    print ("DEU CERTO!")
except:
    print("FODEU!")
    #print ("Não consegui!")


#DESAFIO 115
Crie um pequeno "sistema modularizado" que permita cadastrar pessoas
pelo seu NOME e IDADE em um arquivo de texto simples.

O sistema só vai ter "2 opções": cadastrar uma nova pessoa e "listar"
todas as pessoas cadastradas. 
#RESPOSTA:
#interface\__init__.py
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ("\033[30;41mERRO! Por favor, digite um número válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print ('\033[31;40mO usuário preferiu não digitar.\033[m')
            return 0
        else:
            return n

def linha(tam= 42):
    return "-"*tam

#sistema.py
from time import sleep
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova pessoa", "Sair do sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema, até logo.")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(2)

#arquivo\__init__.py
from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return  False
    else:
        return True


def criarArquivo(nome):
    try:
        a= open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabeçalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:<3}anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a =open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print ("Houve um erro na hora de escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()
