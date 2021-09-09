"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
import math
import sys

num = int(input('Insira um número menor que 1000: '))
if num > 1000:
    print('Número maior que 1000. Encerrando')
    sys.exit()
centenas = math.floor(num/100)
dezenas = math.floor((num%100) / 10)
unidades = num % 10

if centenas > 0:
    print(f'{num} = {centenas} centena(s), {dezenas} dezena(s), {unidades} unidade(s)')
elif centenas == 0 and dezenas > 0:
    print(f'{num} = {dezenas} dezena(s), {unidades} unidade(s)')
elif dezenas == 0 and centenas == 0:
    print(f'{num} = {unidades} unidade(s)')



