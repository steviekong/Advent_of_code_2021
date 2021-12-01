
def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        inputlst.append(int(line.rstrip()))
    
    file.close()
    
    count = 0
    result_lst = []
    for i in range(len(inputlst) - 2):
        result_lst.append(inputlst[i] + inputlst[i+1] + inputlst[i+2])
    
    for i in range(1, len(result_lst)):
        if result_lst[i] > result_lst[i-1]:
            count += 1
        
    print(count)

if __name__ == "__main__":
    main()