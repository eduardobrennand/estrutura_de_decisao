#Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print('O numero {} é maior'.format(n1))
else: 
    print('O numero {} é maior. '.format(n2))
