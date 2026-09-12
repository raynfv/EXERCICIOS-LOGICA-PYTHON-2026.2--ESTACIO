print("""
====================================
       TABUADA DE MULTIPLICAÇÃO
====================================
""")

numero = int(input("Digite um numero inteiro:"))

for i in range(1, 11):
    resultado = numero * i 
    print("{} x {} = {}".format(numero, i, resultado))