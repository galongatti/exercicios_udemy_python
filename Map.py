valores: [int] = []

count: int = 1
while count <= 100:
    valores.append(count)
    count += 1;


def verificarParidade(numero: int):
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero * 3


lista = list(map(verificarParidade, valores))

print(lista)