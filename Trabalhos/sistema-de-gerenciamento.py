
print("""
====================================
   GERENCIAMENTO DE NOTAS DA TURMA
====================================
""")


def cadastrar_aluno():
    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    media = (nota1 + nota2 + nota3) / 3

    return {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }


alunos = []

for i in range(5):
    print("\nCadastro do estudante {}".format(i + 1))
    aluno = cadastrar_aluno()
    alunos.append(aluno)


aprovados = 0
recuperacao = 0
reprovados = 0

maior_media = alunos[0]
menor_media = alunos[0]


for aluno in alunos:

    if aluno["media"] >= 7:
        aprovados = aprovados + 1

    elif aluno["media"] >= 5:
        recuperacao = recuperacao + 1

    else:
        reprovados = reprovados + 1

    if aluno["media"] > maior_media["media"]:
        maior_media = aluno

    if aluno["media"] < menor_media["media"]:
        menor_media = aluno


print("""
====================================
       RESULTADO DA TURMA
====================================
""")

for aluno in alunos:
    print("Nome: {}".format(aluno["nome"]))
    print("Média: {:.2f}".format(aluno["media"]))
    print("------------------------------------")


print("""
====================================
            RESUMO
====================================

Maior média: {} - {:.2f}
Menor média: {} - {:.2f}

Aprovados: {}
Em recuperação: {}
Reprovados: {}

====================================
""".format(
    maior_media["nome"],
    maior_media["media"],
    menor_media["nome"],
    menor_media["media"],
    aprovados,
    recuperacao,
    reprovados
))
