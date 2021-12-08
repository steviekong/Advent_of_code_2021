
def readBoard(lst, i ):
    curr = 0
    board = []
    while curr < 5 and i < len(lst):
        board.append(lst[i].split())
        curr += 1
        i += 1
    return board

def checkWinner(board):

    for row in board:
        all = True
        for i in row:
            if i != "*":
                all = False
        if all:
            return True
    
    for i in range(5):
        all = True
        for row in board:
            if row[i] != "*":
                all = False
        if all:
            return True


    return False


def main():
    file = open("input.txt", "r")

    inputlst = []

    for line in file:
        if line != '\n':
            inputlst.append(line.rstrip())
    
    file.close()

    bingo_nums = []

    boards = []

    i = 0
    while i < len(inputlst):
        if i == 0:
            bingo_nums = inputlst[i].split(",")
            i += 1
        else:
            boards.append(readBoard(inputlst, i))
            i += 5
    
    winner = None
    winner_bingo_num = None
    for i in range(len(bingo_nums)):
        for board in range(len(boards)):
            for row in range(len(boards[board])):
                for val in range(len(boards[board][row])):
                    if boards[board][row][val] == bingo_nums[i]:          
                        boards[board][row][val] = "*"
        
        for board in boards:
            if checkWinner(board):
                winner_bingo_num = bingo_nums[i]
                winner = board
                break
        if winner != None:
            break
    sumVal = 0

    for row in winner:
        for val in row:
            if val != "*":
                sumVal += int(val)
    print(winner_bingo_num)
    print(int(winner_bingo_num) * int(sumVal))

    

    
    

if __name__ == "__main__":
    main()