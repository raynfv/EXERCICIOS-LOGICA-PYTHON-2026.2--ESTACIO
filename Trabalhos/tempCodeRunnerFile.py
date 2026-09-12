print("""
====================================
          CALCULADORA
====================================
""")

numero1 = float (input("Digite o primeiro numero:"))
numero2 = float (input("Digite o segundo numero:"))

print("""
Escolha a operação:

1 - Soma (+)
2 - Subtracao (-)
3 - Multiplicacao (*)
4 - Divisao (/)
5 - Divisao inteira (//)
6 - Resto da divisao (%)
7 - Potencia (**)
""")

opcao = int(input("Digite a operacao desejada:"))

if opcao == 1:
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif opcao == 2:
    resultado = numero1 - numero2
    print("Resultado:", resultado)


elif opcao == 3:
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif opcao == 4:
    if numero2 == 0:
        print("Nao e possivel dividir por zero!")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
   

elif opcao == 5:
    if numero2 == 0:
        print("Nao e possivel dividir por zero!")
    else:
        resultado = numero1 // numero2
        print("Resultado:", resultado)    

elif opcao == 6:
    if numero2 == 0:
        print ("Nao e possivel dividir por zero!")
    else:
        resultado = numero1 % numero2
        print ("Resultado:", resultado)

elif opcao == 7:
    resultado = numero1 ** numero2
    print("Resultado", resultado)

else:
    print("Opcao invalida!")