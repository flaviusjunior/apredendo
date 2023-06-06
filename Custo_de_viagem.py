'''Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km 
para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
distancia = float(input("\nQual a distancia da viagem em KM: "))
acima = distancia * 0.45
abaixo = distancia * 0.50
if (distancia >= 200 ):
    print("\nSua viagem custará R${:.2f}".format(acima))
else:
    print("\nSua viagem custará R${:.2f}".format(abaixo))

'''simplificado "preco = distancia * 0.45 if distancia >= 200 else distancia * 0.50"'''