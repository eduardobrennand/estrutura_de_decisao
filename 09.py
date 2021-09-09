#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('N1: '))
n2 = int(input('N2: '))
n3 = int(input('N3: '))

if n1 > n2 and n2 > n3:
    print('{}, {}, {}'.format(n1, n2, n3))
elif n1 > n3 and n3 > n2:
    print('{}, {}, {}'.format(n1, n3, n2))
elif n2 > n1 and n1 > n3:
    print('{}, {}, {}'.format(n2, n1, n3))
elif n2 > n3 and n3 > n1:
    print('{}, {}, {}'.format(n2, n3, n1))
elif n3 > n1 and n1 > n2:
    print('{}, {}, {}'.format(n3, n1, n2))
elif n3 > n2 and n2 > n1:
    print('{}, {}, {}'.format(n3, n2, n1))