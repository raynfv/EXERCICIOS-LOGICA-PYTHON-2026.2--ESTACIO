print("""
==================================== SITUAÇÃO ACADÊMICA ====================================
""")

nota1 = float(input("Digite a primeira nota:"))

while nota1 < 0 or nota1 > 10:
    print("Nota invalida! Digite uma nota entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota novamente:"))

nota2 = float(input("Digite a segunda nota:"))

while nota2 < 0 or nota2 > 10:
    print("Nota invalida! Digite uma nota entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota novamente:"))

nota3 = float(input("Digite a terceira nota:"))

while nota3 < 0 or nota3 > 10:
    print("Nota invalida! Digite uma nota entre 0 e 10.")
    nota3 = float(input("Digite a terceira nota novamente:"))


media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado!"

elif media >= 5:
    situacao = "Recuperacao."

else:
    situacao = "Reprovado!"


print("""
==================================== RESULTADO ====================================

Nota 1: {: .2f}
Nota 2: {: .2f}
Nota 3: {: .2f}
Media: {: .2f}
Situacao: {}
==================================== """.format(nota1, nota2, nota3, media, situacao))