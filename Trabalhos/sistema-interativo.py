```python
print("""
================================
 GERENCIAMENTO DE NÚMEROS
================================
""")

numeros = []
opcao = -1

while opcao != 0:

    print("""
================================
 GERENCIAMENTO DE NÚMEROS
================================
1 - Cadastrar número
2 - Listar números
3 - Exibir maior número
4 - Exibir menor número
5 - Calcular média
0 - Encerrar programa
""")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        print("Número cadastrado com sucesso!")

    elif opcao == 2:
        print("Números cadastrados:")

        for numero in numeros:
            print(numero)

    elif opcao == 3:
        if len(numeros) > 0:
            print("Maior número: {}".format(max(numeros)))
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 4:
        if len(numeros) > 0:
            print("Menor número: {}".format(min(numeros)))
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 5:
        if len(numeros) > 0:
            media = sum(numeros) / len(numeros)
            print("Média: {:.2f}".format(media))
        else:
            print("Nenhum número cadastrado.")

    elif opcao == 0:
        print("Programa encerrado.")

    else:
        print("Opção inválida.")

