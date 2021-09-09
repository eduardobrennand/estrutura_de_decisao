"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
import math
import sys

print('Informe os valores (ax² + bx + c): ')
a = int(input('a: '))
if a == 0:
    print('Não é uma equação de segundo grau. Encerrando.')
    sys.exit()
else:
    b = int(input('b: '))
    c = int(input('c: '))

delta = (b ** 2) - (4 * a * c)
if delta < 0:
    print('Não possui raízes reais. Encerrando.')
elif delta == 0:
    raiz = -b / (2*a)
    print('Delta = 0. Raíz: {}'.format(raiz))
else:
    x1 = (-b + math.sqrt(delta)) /(2*a )
    x2 = (-b - math.sqrt(delta)) /(2*a )
    print('Possui duas raízes reais, sendo x1 = {:.2f} e x2 = {:.2f}'.format(x1, x2))

