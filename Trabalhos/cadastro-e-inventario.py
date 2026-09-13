print("""
====================================
CONTROLE DE ESTOQUE 
====================================
""")

produtos = []

for i in range(5):
    nome = input("Nome do produto:")
    preco = float(input("Preco do produto:"))
    quantidade = int(input("Quantidade em estoque:"))

    produtos.append({
        "nome" : nome,
        "preco" : preco,
        "quantidade" : quantidade
    })

total_estoque = 0
for produto in produtos:
    total_estoque = total_estoque + (produto["preco"]*produto["quantidade"])

mais_caro = produtos[0]

for produto in produtos:
    if produto["preco"] > mais_caro ["preco"]:
        mais_caro = produto

print("""
====================================
PRODUTOS CADASTRADOS
====================================
""")

for produto in produtos:
    print("Nome: {}" .format(produto["nome"]))
    print("Preco: R$ {: .2f}" .format(produto["preco"]))
    print("Quantidade: {}" .format(produto["quantidade"]))
    print("------------------------------------")

print("""
====================================
         RESUMO DO ESTOQUE
====================================

Valor total do estoque: R$ {: .2f}
Produto com maior preço: {}
Preço unitário: R$ {:.2f}

====================================
""".format(
    total_estoque,
    mais_caro["nome"],
    mais_caro["preco"]

)
      )
