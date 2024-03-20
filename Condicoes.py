# media = int(input('ENTRE COM A SUA MEDIA:'))
# if media >= 60:
#     print('APROVADO')
# else:
#     print('REPROVADO')
'''
#Exercícios - 1
a = float(input('DIGITE A VELOCIDADE DO SEU CARRO EM KM/H:'))
multa = 5 * (a-80)
if a > 80:
    print(f"Você foi multado e deve pagar R${multa}.")
else:
    print('Você não foi multado.')
'''
#Exercícios - 2
a = int(input('Escreva um número:'))
b = int(input('Escreva outro número:'))
c = int(input('Escreva outro número:'))

if a == b == c:
    print('Todos os números são iguais.')
else:
    menor = min(a, b, c)
    maior = max(a, b, c)
    print(f"{menor} é o menor número e {maior} é o maior número.")
'''
#Exercícios - 3
a = float(input('Digite seu salário:'))
if a > 1250:
    print(f'Seu novo salário será {(a * 0.10) + a}')
else:
    print(f'Seu novo salário será {(a * 0.15) + a}')
'''
'''
#Exercícios - 4
a = float(input('Digite a distância de sua viagem em km:'))
if a <= 200:
    print(f'Você deve pagar {(a * 0.50)}.')
else:
    print(f'Você deve pagar {(a * 0.45)}.')
'''
