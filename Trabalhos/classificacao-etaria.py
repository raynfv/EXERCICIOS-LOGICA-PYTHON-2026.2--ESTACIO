print("""
==================================== CLASSIFICAÇÃO ETÁRIA ====================================
""")

idade = int(input("Digite sua idade:"))

while idade < 0:
    print("Idade invalida! A idade não pode ser negativa.")
    idade = int(input("Digite sua idade novamente:"))

if idade <= 12:
    classificacao = "Crianca"

elif idade <= 17:
    classificacao = "Adolescente"

elif idade <= 59:
    classificacao = "Adulto"

else:
    classificacao = "Idoso"

print("""
==================================== RESULTADO ====================================
Idade: {}
Classificacao: {}
==================================== """.format(idade, classificacao))
