def verificar_valor(func):
    def verificar(x1, x2):
        if x1 == 0 or x2 == 0:
            print("Não é possível fazer divisão por zero")
        else:
            return func(x1, x2)


    return verificar


@verificar_valor
def dividir(x1, x2):
    print(x1 / x2)


dividir(10, 0)
