"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""


print('Responda com S de SIM ou N de NÃO: ')
contagem = 0
telefone = input('Telefonou para a vítima? ')
if telefone == 'S':
    contagem = 1
local = input('Esteve no local do crime? ')
if local == 'S':
    contagem = contagem + 1
moradia = input('Mora perto da vítima? ')
if moradia == 'S':
    contagem = contagem + 1
divida = input('Devia pra vítima? ') 
if divida == 'S':
    contagem = contagem + 1
trabalho = input('Já trabalhou com a vítima? ')
if trabalho == 'S':
    contagem = contagem + 1

print('Nível de suspeita = {}'.format(contagem))
if contagem == 2:
    print('Suspeita.')
elif contagem >= 3 and contagem <= 4:
    print('Cúmplice')
elif contagem == 5:
    print('Assassino.')
else:
    print('Inocente.')
