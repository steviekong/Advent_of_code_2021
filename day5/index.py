def isHorizonal(x1, x2):
    if x1 == x2:
        return True
    else:
        return False


def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        if line != '\n':
            inputlst.append(line.rstrip())
    
    file.close()

    maxSizeX = 0
    maxSizeY = 0

    for i in inputlst:
        s = i.split()
        x1, y1 = int(s[0].split(",")[0]), int(s[0].split(",")[1])
        x2, y2 = int(s[2].split(",")[0]), int(s[2].split(",")[1])
        
        maxSizeX = max(maxSizeX, x1, x2)
        maxSizeY = max(maxSizeY, y1, y2)
        

    overlappoints = []

    for i in range(maxSizeX + 1):
        overlappoints.append([])
        for j in range(maxSizeY + 1):
            overlappoints[i].append(0)
    
    for i in inputlst:
        s = i.split()
        x1, y1 = int(s[0].split(",")[0]), int(s[0].split(",")[1])
        x2, y2 = int(s[2].split(",")[0]), int(s[2].split(",")[1])

        if isHorizonal(x1, x2):
            minY = min(y1, y2)
            maxSizeY = max(y1, y2)
            for i in range(int(minY), int(maxSizeY)+1):
                overlappoints[x1][i] += 1    
        elif isHorizonal(y1, y2):
            minX = min(x1, x2)
            maxX = max(x1, x2)
            for i in range(int(minX), int(maxX)+1):
                overlappoints[i][y1] += 1
    overlapCount = 0

    for i in overlappoints:
        for j in i:
            if j > 1:
                overlapCount += 1

    print(overlapCount)
    
if __name__ == "__main__":
    main()