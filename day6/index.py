
def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        inputlst = list(line.split(","))
    inputlst =  list(map(lambda x: int(x), inputlst))
    
    file.close()

    days = [0] * 9
    for i in inputlst:
        days[i] += 1

    for i in range(256):
        zeroVal = days.pop(0)
        days.append(0)
        
        days[6] += zeroVal
        days[8] += zeroVal


        

    print(days)
    total = 0
    for i in range(9):
        total += days[i]
    print(total)
    


if __name__ == "__main__":
    main()

# 1 fish 43 other fish