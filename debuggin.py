def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Termino programa")


if __name__ == '__main__':
    main()
