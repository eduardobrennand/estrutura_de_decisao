#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
import math

n = float(input('Digite um número: '))
if n - math.floor(n) == 0:
    print('Número inteiro!')
else:
    print('Número decimal!')