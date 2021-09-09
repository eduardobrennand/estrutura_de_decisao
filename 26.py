"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro. 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina).
Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = int(input('Quantos litros deseja abastecer? '))
tipo = input('Qual tipo de combustível desejado? A-Álcool, G-Gasolina   ')
preço = 0

if tipo == 'A' or tipo == 'a':
    tipo = 'álcool'
    preço = 1.90 * litros
    if litros <= 20:
        preço = preço * 0.97
    else:
        preço = preço * 0.95
elif tipo == 'G' or tipo == 'g':
    tipo = 'gasolina'
    preço = 2.50 * litros
    if litros <= 20:
        preço = preço * 0.96
    else:
        preço = preço * 0.94
else:
    print('Tipo inválido. Digite A ou G.')

print(f'O preço do abastecimento de {litros}L de {tipo} é R${preço}')

