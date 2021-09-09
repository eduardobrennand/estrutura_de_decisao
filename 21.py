"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
import math

valor_original = int(input('Valor do saque: '))
notas_100 = int(valor_original / 100)
valor = valor_original - (100 * notas_100)
notas_50 = int(valor / 50)
valor = valor - (50 * notas_50)
notas_10 = int(valor / 10)
valor = valor - (10 * notas_10)
notas_5 = int(valor / 5)
valor = valor - (5 * notas_5)
notas_1 = int(valor / 1)

print(f'Para sacar {valor_original}, são necessárias {notas_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} notas de 5, {notas_1} notas de 1.')