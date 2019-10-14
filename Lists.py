if __name__ == '__main__':
    N = int(input())

    lista = []
    for i in range(N):
        operation, *args = input().split()

        arguments = list(map(int, args))

        if(operation == 'insert'):
            lista.insert(arguments[0], arguments[1])

        elif(operation == 'print'):
            print(lista)

        elif(operation == 'remove'):
            lista.remove(arguments[0])

        elif(operation == 'append'):
            lista.append(arguments[0])

        elif(operation == 'sort'):
            lista.sort()

        elif(operation == 'pop'):
            lista.pop(len(lista) - 1)

        elif(operation == 'reverse'):
            lista.reverse()
