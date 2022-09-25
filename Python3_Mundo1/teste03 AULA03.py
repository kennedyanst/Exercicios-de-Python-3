nx = input('Digite algo:')
print('Os dados do seu caracterer é:')
print ('O tipo primitivo:', type(nx))
print ('é numerico?', (nx.isnumeric()))
print ('é alfabetico?', (nx.isalpha()))
print ('é alfanumerico?',(nx.isalnum()))
print ('é maiusculo?', (nx.isupper()))
print ('é minusculo?',(nx.islower()))
print ('os caracteres são imprimiveis?', (nx.isprintable()))

n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número:'))
s = n1 + n2
print ('A soma entre {} e {} equivale à:{}'.format(n1,n2,s))
