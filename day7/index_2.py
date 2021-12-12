
def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        inputlst = list(line.split(","))
    inputlst =  list(map(lambda x: int(x), inputlst))
    
    file.close()

    valuesSet = set(inputlst)
    minSum = float("inf")
    q = None
    maxVal = max(valuesSet)
    for val in range(maxVal):
        sum = 0
        for i in inputlst:
            n = abs(val - i)
            sum += n * (n + 1) // 2
        if sum < minSum:
            minSum = sum
    print(minSum)
 
if __name__ == "__main__":
    main()
