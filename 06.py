#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

if n1 > n2 and n1 > n3:
    print('N1 é o maior. {} > {} e {}'.format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('N2 é o maior. {} > {} e {}'.format(n2, n1, n3))
elif n3 > n1 and n3 > n2:
    print('N3 é o maior. {} > {} e {}'.format(n3, n1, n2))