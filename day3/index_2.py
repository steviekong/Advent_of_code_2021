
def main():
    file = open("input.txt", "r")

    inputlst = []

    for i in file:
        inputlst.append(i.strip())
    file.close()

    copy_lst = inputlst.copy()

    for k in range(len(inputlst[0])):
        if len(inputlst) == 1:
            break
        result_lst_zero = 0
        result_lst_one = 0
        for i in inputlst:
            if i[k] == "1":
                result_lst_one += 1
            elif i[k] == "0":
                result_lst_zero += 1
        if result_lst_zero > result_lst_one:
            inputlst = list(filter(lambda x: x[k] == "0", inputlst))
        else:
            inputlst = list(filter(lambda x: x[k] == "1", inputlst))

    for k in range(len(copy_lst[0])):
        if len(copy_lst) == 1:
            break
        result_lst_zero = 0
        result_lst_one = 0
        for i in copy_lst:
            if i[k] == "1":
                result_lst_one += 1
            elif i[k] == "0":
                result_lst_zero += 1
        if result_lst_zero <= result_lst_one:
            copy_lst = list(filter(lambda x: x[k] == "0", copy_lst))
        else:
            copy_lst = list(filter(lambda x: x[k] == "1", copy_lst))


    print(int(inputlst[0], 2) * int(copy_lst[0], 2))
            


    

if __name__ == "__main__":
    main()