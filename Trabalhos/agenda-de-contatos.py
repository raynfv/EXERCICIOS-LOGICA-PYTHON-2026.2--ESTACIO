
print("""
====================================
       AGENDA DE CONTATOS
====================================
""")

contatos = []

for i in range(5):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })

busca = input("\nDigite o nome que deseja consultar: ")

encontrado = False

for contato in contatos:
    if contato["nome"] == busca:
        print("""
====================================
       CONTATO ENCONTRADO
====================================
Nome: {}
Telefone: {}
E-mail: {}
====================================
""".format(
            contato["nome"],
            contato["telefone"],
            contato["email"]
        ))

        encontrado = True

if encontrado == False:
    print("Contato não encontrado.")



