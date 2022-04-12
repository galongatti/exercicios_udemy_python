def verificar_divisivel(valor: float):
    """

    :param valor: valor a ser verificado
    :return: uma palavra de acordo com o valor
    """
    if valor % 2 == 0:
        return "Fizz"
    elif valor % 5 == 0 and valor % 3 == 0:
        return "FizzBuzz"
    elif valor % 5 == 0:
        return "Buzz"
    else:
        return valor

print(verificar_divisivel.__doc__)
print(verificar_divisivel(9))
