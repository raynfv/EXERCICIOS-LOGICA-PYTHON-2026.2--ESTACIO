print(""" ==================================== ORDENAÇÃO DE TRÊS NÚMEROS ==================================== """)


numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
numero3 = int(input("Digite o terceiro numero:"))

if numero1 > numero2:

    if numero1 > numero3:

        maior = numero1

        if numero2 > numero3:
            mediana = numero2
            menor = numero3

        else:
            mediana = numero3
            menor = numero2

    else:
        maior = numero3
        mediana = numero1
        menor = numero2

else:

    if numero2 > numero3:

        maior = numero2

        if numero1 > numero3:
            mediana = numero1
            menor = numero3
        else:
            mediana = numero3
            menor = numero1

    else:
        maior = numero3
        mediana = numero2
        menor = numero1


print(""" ==================================== RESULTADO ==================================== 
Maior número: {} 
Número mediano: {} 
Menor número: {} 
==================================== """.format(maior, mediana, menor))
