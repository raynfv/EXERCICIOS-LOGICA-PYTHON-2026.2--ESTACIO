clientes = []
print("""================================
       CRIAR MINHA CONTA
================================

Vamos começar seu cadastro!""")

nome = input("Digite seu nome completo:")
idade = input ("Digite a sua idade:")
altura = input ("Digite as sua altura:")
cidade = input ("Digite a sua cidade:")

clientes.append({
    'nome': nome,
    'idade': idade,
    'altura': altura, 
    'cidade': cidade
})

print("""
====================================
       CARTÃO DE IDENTIFICAÇÃO
====================================
Nome:    {}
Idade:   {} anos
Altura:  {} m
Cidade:  {}
====================================
""".format(nome, idade, altura, cidade))