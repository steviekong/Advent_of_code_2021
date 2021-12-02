
def main():
    file = open("input.txt", "r")

    inputlst = []

    horizontal = 0
    vertical = 0
    aim = 0

    for i in file:
        inputlst.append(i.strip())

    for i in inputlst:
        s = i.split(" ")
        if s[0] == "forward":
            horizontal += int(s[1])
            vertical += aim * int(s[1])
        elif s[0] == "up":
            aim -= int(s[1])
            
        elif s[0] == "down":
            aim +=  int(s[1])
            
    print(horizontal, vertical)
    print(horizontal * vertical)

if __name__ == "__main__":
    main()