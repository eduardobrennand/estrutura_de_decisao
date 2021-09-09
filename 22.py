#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num = int(input('Digite um númnero: '))


if num % 2: #Nesse caso, utilizo o valor booleano, no caso do valor ser 1 ou true, cai no ímpar. Caso o valor seja 0 ou false, cai no par (else)
    print('É ímpar!')
else:
    print('É par!')