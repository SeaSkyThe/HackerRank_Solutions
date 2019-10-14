if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])


    #print(len(students))

#Creating dictionary with the list
students_dic = {}
for i in students:
    students_dic[i[0]] = i[1]

students_dic_ord = {}

#sorting the dictionary
for key, value in sorted(students_dic.items(), key=lambda kv: kv[1]):
    students_dic_ord[key] = value
    #print("%s: %f" % (key, value))

#creating a list with the sorted data
students = []
for key, value in students_dic_ord.items():
    temp = [key,value]
    students.append(temp)
#print(students)

def get_sec_lowest(array):
    students_second_lowest = []
    lowest = array[0][1]

    flag = 1
    while(flag):
        if array[0][1] == lowest:
            array.pop(0)
            print(array)
        else:
            flag = 0

    students_second_lowest.append(array[0])
    for i in range(1, len(array)):
        if(students_second_lowest[0][1] == array[i][1]):
            students_second_lowest.append(array[i])

    return students_second_lowest

lowest = []
for student in get_sec_lowest(students):
    lowest.append(student[0])

lowest.sort()
for i in lowest:
    print (i)
