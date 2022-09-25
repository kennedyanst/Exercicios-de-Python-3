#DESAFIO 16
from math import trunc
n1 = float(input('Digite um número real:'))
s = trunc(n1)
print ('A porção inteira do seu número é: {}!'.format(s))

#DESAFIO 17
catop = int(input('Digite o cateto oposto:'))
catad = int(input('Digite o cateto adjacente:'))
s = catad**2 + catop**2
hip = s**(1/2)
print ('O resultado da hipotenusa é {}.'.format(hip))

#DESAFIO 18
import math
n = float(input('Digite o valor do ângulo:'))
sen = math.sin(math.radians(n))
coss = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print ('O seno é: {}, o cosseno {} e a tangente{}.'.format(sen, coss, tg))

#DESAFIO 19
import random
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')
lista = [a1,a2,a3,a4]
escolha = random.choice(lista)
print ('Parabéns, {}!! Você foi o aluno escolhi!'.format(escolha))

#DESAFIO 20
import random
a1 = input('Digite o nome do aluno 1:')
a2 = input('Digite o nome do aluno 2:')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4:')
lista = [a1,a2,a3,a4]
escolha = random.sample(lista,4)
print ('Parabéns, {}!! Você foi o aluno escolhi!'.format(escolha))

#DESAFIO 21
import pygame
pygame.init()
pygame.mixer.music.load('house_lo.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
