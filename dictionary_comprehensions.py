import math


def main():
    # my_dic = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dic[i] = i**3

    # my_dic = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dic)

    my_dic = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}
    print(my_dic)


if __name__ == '__main__':
    main()
