#DESAFIO 5
n1 = int(input('Digite um número inteiro!'))
s = n1+1
a = n1-1
print ('O sucessor de {}: é {} e o seu antecessor é: {}.'.format(n1,s,a))

#DESAFIO 6
n1 = int(input('Digite um número:'))
dob = n1*2
trip = n1*3
raiz = n1**(1/2)
print ('O dobro de {} é {}, o seu triplo é {}, e a sua raiz quadrada é {}'.format(n1,dob,trip,raiz))

#DESAFIO 7
nome = input ('Digite seu nome:')
n1 = int(input ('digite a primeira nota:'))
n2 = int(input ('digite a segunda nota:'))
s = (n1 + n2)/2
print (' {} A média entre {} e {} é igual a {}'.format (nome,n1, n2, s))

#Desafio 8
n1 = int(input('Digite o número em metros:'))
cm = n1*100
mm = n1*1000
print ('{} = cm{} e em mm{}'.format(n1,cm,mm))

#DESAFIO 9
n = int(input('Digite um número para saber sua tabuada:'))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print ('A Tabuada do {} é:'.format(n))
print ('\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))

#DESAFIO10
nome = input('Digite seu nome:')
n1 = int(input('Digite a quantos reais tem na sau carteira:'))
dol = n1*3.27
print ('{}, pode comprar {} dolares com {} reais.'.format(nome,dol,n1))

#DESAFIO11
lar = int(input('Digite a largura da parede:'))
alt = int (input('Digite a altura da parede:'))
area = alt*lar
tint = area/2
print ('A area da sua parede é: {}m².'.format(area))
print ('A quantidade de tinta necessária é de: {} litros!'.format(tint))

#DESAFIO 12
n1 = int(input('Digite o preço do produto:'))
s = n1*0.95
print ('O valor do produto com 5% de desconto fica: {}'.format(s))

#DESAFIO13
n1 = int(input('Digite o seu salario:'))
s = n1*1.15
print ('O valor do seu salario com 15% de aumento fica: {}'.format(s))
