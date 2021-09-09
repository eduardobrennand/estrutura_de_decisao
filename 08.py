#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Preço 1: '))
p2 = float(input('Preço 2: '))
p3 = float(input('Preço 3: '))

if p1 < p2 and p1 < p3:
    print('Compre o produto 1.')
elif p2 < p1 and p2 < p3:
    print('Compre o produto 2.')
elif p3 < p1 and p3 < p2:
    print('Compre o produto 3.')