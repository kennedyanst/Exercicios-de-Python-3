#DESAFIO 28
import random
print ('Qual número entre 0 e 5 eu pensei?')
n1 = random.randint(0,5)
resp = int(input('Digite a resposta:'))
if resp == n1:
    print ('Você acertou!')
else:
    print ('Você errou!!')
    
#DESAFIO 29
s = int(input('Digite a delta "S" em KM:'))
t = int(input('Digite o delta "T" em Hora'))
velo = s/t
multa = (velo - 80)*7
if velo >= 80:
    print ('Burro filho da puta! Sua velocidade é de {}KM/H e você foi multado.'.format(velo))
    print ('Sua multa é de: {}'. format(multa))
else:
    print ('Sua velocidade é de {} KM/H, ta suave!'. format(velo))

#DESAFIO 30
num = int(input('Digite um número inteiro:'))
resto = num % 2
if resto==0:
    print ('Seu número é par!')
else:
    print ('Seu número é impar!')

#DESAFIO 31
dist = int(input('Digite a distância da viagem em km:'))
valor1 = dist * 0.50
valor2 = dist * 0.45
if dist <=200:
    print ('O valor da passagem é de: {}. '.format(valor1))
else:
    print ('O valor da passagem é de {}.'.format(valor2))

#DESAFIO 32
ano = int(input('Digite o ano para saber se ele é bissexto:'))
if ano%4==0:
    print ('Seu ano é bissexto!')
else:
    print ('Seu ano não é bissexto')

#DESAFIO 33
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite mais um número:'))
lista = [num1, num2, num3]
print ('O maior número é:{}, e o menor número é:{}.'.format (max(lista), min(lista)))

#DESAFIO 34
sal = float(input('Digite o seu salário:'))
aum1 = sal * 1.10
aum2 = sal * 1.15
if sal >= 1250.00:
    print ('Seu aumento é de: 10%, e seu sálario atual ficará:{:.2f}.'. format(aum1))
else:
    print ('Seu aumento é de 15%, e o seu salário atual ficará:{:.2f}'. format(aum2))

#DESAFIO 35
a = int(input('DIGITE UM VALOR:'))
b = int(input('DIGITE UM LADO:'))
c = int(input('DIGITE UM LADO:'))
formula1 = a + b > c
formula2 = a + c > b
formula3 = c + b > a
if formula3 and formula2 and formula1:
    print ('É um triângulo!')
else:
    print ('Não é um triângulo!')
