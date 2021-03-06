"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
print('Nota 1: {} \nNota 2: {} \n Média: {}'.format(n1,n2,media))

if media >= 9 and media <= 10:
    print('Aprovado! Conceito A!')
elif media >= 7.5 and media < 9:
    print('Aprovado! Conceito B!')
elif media >= 6 and media < 7.5:
    print('Aprovado! Conceito C!')
elif media >= 4 and media < 6:
    print('Reprovado! Conceito D!')
elif media < 4:
    print('Reprovado! Conceito E!')
