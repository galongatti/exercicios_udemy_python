valores: [int] = []

count: int = 1
while count <= 100:
    valores.append(count)
    count += 1;

def verificarParidade(numero: int):
    if numero % 2 == 0:
        return True
    else:
        return False

numeros_extraidos:  [int] = filter(verificarParidade, valores)

print(list(numeros_extraidos))