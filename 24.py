"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""
import math

n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))

operaçao = input('Qual operação desejar realizar? (A de adição), (S de subtração), (M de multiplicação) ou (D de divisão)')
resultado = None

if operaçao == 'A' or operaçao == 'a':
    resultado = n1 + n2
elif operaçao == 'S' or operaçao == 's':
    resultado = n1 - n2
elif operaçao == 'M' or operaçao == 'm':
    resultado = n1 * n2
elif operaçao == 'D' or operaçao == 'd':
    resultado = n1 / n2

print('O resultado da sua operação é: {}'.format(resultado))

if resultado % 2:
    print('Ímpar')
else:
    print('Par')

if resultado >= 0:
    print('Positivo')
else:
    print('Negativo')

if resultado - math.floor(resultado) == 0:
    print('Inteiro')
else:
    print('Decimal')