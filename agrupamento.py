from itertools import groupby

alunos = [
    {'nome' : 'JOÃO', 'nota': 'A'},
    {'nome' : 'AMANDA', 'nota': 'A'},
    {'nome' : 'CARLOS', 'nota': 'A'},
    {'nome' : 'PAULA', 'nota': 'B'},
    {'nome' : 'PEDRO', 'nota': 'D'},
    {'nome' : 'RENATA', 'nota': 'C'},
    {'nome' : 'KAROL', 'nota': 'C'},
    {'nome' : 'ISABELA', 'nota': 'A'},
    {'nome' : 'GERALDO', 'nota': 'B'},
    {'nome' : 'ANA', 'nota': 'D'}
]

alunos.sort(key=lambda alunos: [alunos['nota'],alunos['nome']], reverse=False)
alunos_agrupados = groupby(alunos, lambda alunos: alunos['nota'])

for nota, alunos_agr in alunos_agrupados:
    print(f"\tNota: {nota}")
    count = 0
    for a in alunos_agr:
        print(f"\tAluno: {a['nome']}")
        count += 1

    print(f"\tTotal de alunos com a nota {nota} : {count}")


