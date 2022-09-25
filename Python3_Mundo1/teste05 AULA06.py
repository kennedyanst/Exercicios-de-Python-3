n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
restdiv = n1%n2
print ('A soma é: {}, a subtração é: {}, a mutiplicação é: {}'.format(s,sub,m))
print ('a divisão até 3 casas decimais é: {:.3f}, a divisão inteira é:{} o resto da divisão é:{}'.format(d,di,restdiv))
