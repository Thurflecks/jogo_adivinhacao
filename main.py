from random import randint


nome = input('Se foda miseravel, qual o seu nome desgraçado? ')
print(f'Ok {nome}, estou escolhendo um número de 1 ate 10. Se não adivinhar você dar a bunda!!!')

numero = randint(1,10)
tentativas = 3

for tentativa in range(1, tentativas + 1):
    numero_esco = int(input('Diz um número ai fi de corno?: '))

    if numero_esco == numero:
        print(f'Acertou miseravii, em {tentativa} tentativas')
        break
 
    elif numero_esco > numero:
        print('Escolha um numero menor fella')
    
    else:
        print('Escolha um numero maior, fella')

print(f'Obrigado por perder seu tempo {nome}, o número era {numero}')



    
