""" Exibe relatoio de crianças por atividades.
Imprimir a lista de crianças agrupadas por sala que frequenta cada uma das atividades.
"""
# __version__ "0.1.0"

# listas

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Artur", "Maria", "Isabela"]

aula_ingles = ["Erik", "Maia", "Joana", "Artur", "Antonio"]
aula_musica = ["Erik", "Artur", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Imprimir quais os alunos separados por sala
# Listar alunos

atividades = [
    ("Inglês ", aula_ingles),
    ("Música ", aula_musica),
    ("Dança ", aula_danca),
]

# Listar alunos em cada atividade por sala
for nome_atividade, atividade in atividades:
    
    print(f"Alunos da atividade --> {nome_atividade}\n")
    print(f"-" * 50)

    atividade_sala1 = []
    atividade_sala2 = []
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
print("Sala1 ", atividade_sala1)
print("Sala2 ", atividade_sala2)
print()
print("-" * 50)




