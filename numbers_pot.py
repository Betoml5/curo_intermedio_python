import math


def main():
    # my_list = []
    # for number in range(1, 101):
    #     if number % 3 != 0:
    #         number_powed = pow(number, 2)
    #         my_list.append(number_powed)

    # squares = [i**2 for i in range(1, 101) if number % 3 != 0]
    # print(squares)

    my_numbers = [i for i in range(1, 1001) if i % 36 == 0]

    print(my_numbers)


if __name__ == '__main__':
    main()
