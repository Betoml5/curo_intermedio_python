from functools import reduce


def main():
    my_list = [1, 2, 3, 4]

    result = list(filter(lambda x:  x % 2 != 0, my_list))
    result_2 = list(map(lambda x: x**2, my_list))

    all_multiplied = reduce(lambda a, b: a*b,  my_list)

    print(all_multiplied)
    print(result)
    print(result_2)


if __name__ == '__main__':
    main()
