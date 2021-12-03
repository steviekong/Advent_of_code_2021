
def main():
    file = open("input.txt", "r")

    inputlst = []

    for i in file:
        inputlst.append(i.strip())
    file.close()

    result_lst_zero = [0] * len(inputlst[0])
    result_lst_one = [0] * len(inputlst[0])

    for i in inputlst:
        for b in range(len(i)):
            if i[b] == "1":
                result_lst_one[b] += 1
            elif i[b] == "0":
                result_lst_zero[b] += 1

    gamma_rate = ""

    for i in range(len(result_lst_zero)):
        if result_lst_zero[i] > result_lst_one[i]:
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    gamma_rate  = int(gamma_rate, 2)

    epsilon_rate = gamma_rate ^ 0b111111111111

    print(gamma_rate * epsilon_rate)
            


    

if __name__ == "__main__":
    main()