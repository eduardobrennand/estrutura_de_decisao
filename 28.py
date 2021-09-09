"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
carne = input('Qual tipo de carne você deseja?\n Filé Duplo (FD)\n Alcatra (A)\n Picanha (P)\n ')
kg = int(input('Quantos KG(s)? '))
pagamento = input('Cartão Tabajara? Sim(S) ou Não(N) ')
preço = 0

if carne == 'FD':
    carne = 'Filé Duplo'
    if kg <= 5:
        preço = 4.9 * kg
    else:
        preço = 5.8 * kg
elif carne == 'A':
    carne = 'Alcatra'
    if kg <= 5:
        preço = 5.9 * kg
    else:
        preço = 6.8  * kg
elif carne == 'P':
    carne = 'Picanha'
    if kg <= 5:
        preço = 6.9 * kg
    else: 
        preço = 7.8 * kg
if pagamento == 'S':
    pagamento = 'Cartão Tabajara'
    desconto = preço * 0.05
    valor_pagamento = preço - desconto
else:
    pagamento = 'Dinheiro'
    desconto = 0
    valor_pagamento = preço

print(f'Nota Fiscal: \nTipo de Carne: {carne} \nTotal de KG(s): {kg} \nPreço Total: R${preço} \nTipo de Pagamento: {pagamento} \nValor do Desconto: R${desconto} \nValor a Pagar: R${valor_pagamento} ')