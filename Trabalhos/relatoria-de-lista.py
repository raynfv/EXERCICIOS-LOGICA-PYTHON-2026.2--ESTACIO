print("""
==================================== 
RELATÓRIO DE LISTA NUMÉRICA 
====================================
""")

numeros = []

for i in range(10):
    numero = int(input("Digite um numero inteiro:"))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

soma = sum (numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("""
==================================== 
RELATÓRIO 
====================================

numeros informados: {}
numeros pares: {}
numeros impares: {}
soma: {}
media: {}
maior valor: {}
menor valor: {}

==================================== """.format(numeros, pares, impares, soma, media, maior, menor))
