#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

if letra.isalpha():
    if letra == 'a':
        print('Vogal!')
    elif letra == 'e':
        print('Vogal!')
    elif letra == 'i':
        print('Vogal!')
    elif letra == 'o':
        print('Vogal!')
    elif letra == 'u':
        print('Vogal!')
    else: 
        print('Consoante!')
else:
    print('Não é letra!')