print(""" 
==================================== ANÁLISE DO NÚMERO ==================================== 
""")

numero = int(input("Digite um numero inteiro:"))

if numero > 0:
    sinal = "positivo"

elif numero < 0:
    sinal = "negativo"

else:
    sinal = "nulo"

if numero % 2 == 0:
    paridade = "par"

else:
    paridade = "ímpar"

print("O numero {} é {} e {}. ".format(numero, sinal, paridade))