#DESAFIO 78
listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'\033[1;31mDigite um número na posição \033[97m{c}: \033[m')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print ('\033[30m-*\033[m'*20)
print (f'\033[107;30;3mA lista ficou {listanum}\033[m')
print (f'\033[1;97mO maior é: {maior} na posição: ', end='')
for i,v in enumerate(listanum):
    if v == maior:
        print (f'{i}...', end='')
print()
print (f'O menor é: {menor} na posição: ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print (f'{i}...', end='')
print()

#DESAFIO 79
numero = list()
while True:
    n = int(input('\033[3;107;32mDigite um número:\033[m '))
    if n not in numero:
        numero.append(n)
        print ('\033[1;32mNúmero adicionado com \033[4mSUCESSO...\033[m')
    else:
        print ('\033[30;41;1;4mNÚMERO REPETIDO, DIGITE NOVAMENTE!!\033[m')
    r = str(input('\033[3;36mQuer continuar? [S/N]\033[m')).strip().upper()[0]
    if r == 'N':
        break
print ('\033[30m-=\033[m'*15)
print ('\033[1;97mFIM DO PROGRAMA!\033[m')
print (f'\033[35mOs números são {sorted(numero)}')

#DESAFIO 80
lista =[]
for c in range(0,5):
     n = int(input('Digite um número: '))
     if c == 0 or n > lista[-1]:
          lista.append(n)
     else:
          pos = 0
          while pos < len(lista):
               if n <= lista[pos]:
                    lista.insert(pos, n)
                    break
               pos += 1
print (f'A ordem da lista ficou: {lista}')

#DESAFIO 81
lista = []
while True:
    lista.append(int(input('\033[4mDigite um número:\033[m ')))
    opcao = str(input('\033[1mQuer continuar? [S/N]:\033[m ')).strip().upper()[0]
    if opcao == 'N':
        break
print ('\033[1;30m-=\033[m'*20)
print(f'\033[1;3;97mA quantidade de elementos digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista decrescente fica: {lista}')
if 5 in lista:
    print ('O valor 5 FAZ PARTE da lista!')
else:
    print ('O valor 5 NÃO FAZ PARTE da lista!')

#DESAFIO 82
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    opcao = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print (f'-='*20)
print (f'Lista completa: {lista.sort()}')
print (f'Lista par: {listapar}')
print (f'Lista impar: {listaimpar}')

#DESAFIO 83
expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print ('Sua expressão é válida!')
else:
    print ('Sua expressão é inválida!!')
