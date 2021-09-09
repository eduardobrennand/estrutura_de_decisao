"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input('Valor do salário: '))
percentual = None
aumento = None
novo_salario = None

if salario < 280:
    percentual = '20%'
    novo_salario = salario * 1.20
    aumento = novo_salario - salario
elif salario >= 280 and salario < 700:
    percentual = '15%'
    novo_salario = salario * 1.15
    aumento = novo_salario - salario
elif salario >= 700 and salario < 1500:
    percentual = '10%'
    novo_salario = salario * 1.10
    aumento = novo_salario - salario
else:
    percentual = '5%'
    novo_salario = salario * 1.05
    aumento = novo_salario - salario

print(f'Seu salário era de R${salario}, com um aumento de {percentual}, seu novo salário é de R${novo_salario}. Agora você ganha R${aumento} a mais que antes!')

    