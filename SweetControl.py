
loja = "Confeitaria Sweet Control"

print("""╔════════════════════════════════════════════╗
║              🍰 SWEETCONTROL               ║
║          Confeitaria Sweet Control         ║
╚════════════════════════════════════════════╝

              MENU PRINCIPAL

  👤 MINHA CONTA
  ──────────────────────────────────────────
  1 - Criar minha conta
  2 - Entrar
  3 - Meu perfil

  🍰 PRODUTOS
  ──────────────────────────────────────────
  4 - Ver produtos
  5 - Buscar produto
  6 - Ver detalhes do produto

  🛒 MEUS PEDIDOS
  ──────────────────────────────────────────
  7 - Fazer pedido
  8 - Meus pedidos
  9 - Acompanhar pedido
  10 - Cancelar pedido

  💳 PAGAMENTO
  ──────────────────────────────────────────
  11 - Escolher forma de pagamento
  12 - Ver pagamento

  📞 ATENDIMENTO
  ──────────────────────────────────────────
  13 - Entrar em contato
  14 - Perguntas frequentes

  ──────────────────────────────────────────
  0 - Sair
  ──────────────────────────────────────────
""")

clientes = []

opcao = int(input("Digite a opcao que voce deseja: "))

if opcao == 1:

    print("""================================
       CRIAR MINHA CONTA
================================

Vamos começar seu cadastro!""")

    clientes.append({
        'nome': input("Nome: "),
        'telefone': input("Telefone: "),
        'email': input("E-mail: "),
        'senha': input("Senha: ")
    })

    print(f"""================================
       CONTA CRIADA! 🎉
================================

Bem-vindo ao SweetControl, {clientes[0]["nome"]}!
""")

