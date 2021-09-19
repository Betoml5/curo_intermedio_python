def main():
    # try:
    #     numero = int(input("Ingresa un numero"))
    #     numero = numero * numero
    #     print(numero)
    # except ValueError as te:
    #     print("Solo se pueden ingresar numeros", te)
    numero = input("Ingresa un numero")
    print(numero.isnumeric())
    assert numero.isnumeric(), "Debes ingresar un numero, no una cadena de caracteres"


if __name__ == '__main__':
    main()
