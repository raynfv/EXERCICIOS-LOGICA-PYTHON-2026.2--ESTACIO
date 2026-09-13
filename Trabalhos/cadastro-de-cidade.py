print("""
====================================
     CADASTRO DE CIDADES
====================================
""")

cidades = []

for i in range(5):
    print("\nCadastro da cidade {}".format(i + 1))

    nome = input("Nome da cidade: ")
    estado = input("Estado (sigla): ")
    populacao = int(input("População estimada: "))

    cidades.append({
        "nome": nome,
        "estado": estado,
        "populacao": populacao
    })


maior = cidades[0]
menor = cidades[0]
total = 0

for cidade in cidades:

    total = total + cidade["populacao"]

    if cidade["populacao"] > maior["populacao"]:
        maior = cidade

    if cidade["populacao"] < menor["populacao"]:
        menor = cidade


media = total / len(cidades)


print("""
====================================
       ANÁLISE POPULACIONAL
====================================

Cidade com maior população:
{} - {} | {:,} habitantes

Cidade com menor população:
{} - {} | {:,} habitantes

População total: {:,} habitantes
Média populacional: {:.2f} habitantes

====================================
       CIDADES CADASTRADAS
====================================
""".format(
    maior["nome"],
    maior["estado"],
    maior["populacao"],
    menor["nome"],
    menor["estado"],
    menor["populacao"],
    total,
    media
))


for cidade in cidades:
    print("Nome: {}".format(cidade["nome"]))
    print("Estado: {}".format(cidade["estado"]))
    print("População: {:,} habitantes".format(cidade["populacao"]))
    print("------------------------------------")
