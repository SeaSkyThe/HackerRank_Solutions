if __name__ == '__main__':
    n = 5
    arr = [57, 57, -57, 57]

    first = 0
    second = 0
    for i in arr:
        if(i > first):
            first = i

    arr_cpy = list(filter(lambda a: a != first, arr))


    print(arr_cpy)
    for j in arr_cpy:
        if(j > second):
            second = j


    print(second)
