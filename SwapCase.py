def swap_case(s):
    cpy_s = []
    for each in s:
        if(each.islower()):
            cpy_s.append(each.upper())
        else:
            cpy_s.append(each.lower())

    return (''.join(str (item) for item in cpy_s))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
