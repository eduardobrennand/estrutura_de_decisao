"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este 
total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago 
pelo cliente.
"""
morango = int(input('Quantos KG(s) de morango você deseja comprar? '))
maça = int(input('Quantos KG(s) de maçã você deseja comprar? '))
preço_morango = 0
preço_maça = 0

if morango <= 5:
    preço_morango = 2.5 * morango
else:
    preço_morango = 2.2 * morango
if maça <= 5:
    preço_maça = 1.8 * maça
else:
    preço_maça = 1.5 * maça

preço = preço_maça + preço_morango
kg = maça + morango

if preço > 25 or kg > 8:
    preço = preço * 0.9

print(f'Comprando {morango}KG(s) de morango e {maça}KG(s) de maçã, o preço total a ser pago é igual a R${preço}')
