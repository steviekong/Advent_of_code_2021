
def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        inputlst = list(line.split(","))
    inputlst =  list(map(lambda x: int(x), inputlst))
    
    file.close()

    valuesSet = set(inputlst)
    minSum = float("inf")
    for val in valuesSet:
        sum = 0
        for i in inputlst:
            sum += abs(val - i)
        if sum < minSum:
            minSum = sum
    print(minSum)
 
if __name__ == "__main__":
    main()
