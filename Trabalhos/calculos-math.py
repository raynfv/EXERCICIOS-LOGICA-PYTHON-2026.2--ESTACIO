import math

print("""
====================================
       CÁLCULOS MATEMÁTICOS
====================================
""")

numero = float(input("Digite um número real: "))

raiz = math.sqrt(numero)
absoluto = math.fabs(numero)
teto = math.ceil(numero)
piso = math.floor(numero)

print("""
====================================
             RESULTADOS
====================================

Raiz quadrada: {:.2f}
Valor absoluto: {:.2f}
Arredondamento para cima: {}
Arredondamento para baixo: {}
""".format(raiz, absoluto, teto, piso))

if numero >= 0 and numero.is_integer():
    fatorial = math.factorial(int(numero))
    print("Fatorial: {}".format(fatorial))
else:
    print("Fatorial não disponível: o número deve ser inteiro e não negativo.")

print("""
====================================
""")

