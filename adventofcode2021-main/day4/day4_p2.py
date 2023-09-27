def main():
    # read files & get respective lists
    calls = open('calls2.txt', 'r').readlines()[0].split(',')
    boards = getBoards(open('boards2.txt', 'r').readlines())

    # isWinningBoardFound = False
    winningBoard = []
    counter = 0

    tempBoards = boards

    while counter < len(calls):
        # loop through boards
        for i in range(0, len(boards)):
            # loop through board row
            for j in range(0, len(boards[i])):
                for k in range(0, len(boards[i][j])):
                    # print("i: " + str(i) + ", j: " + str(j) + ", k: " + str(k))
                    # print("board item: "+str(boards[i][j][k]))
                    # print("call: "+str(calls[counter]))
                    if boards[i][j][k] == calls[counter]:
                        boards[i][j][k] = "X"
                        tempBoards[i][j][k] = "X"

                    # check for winner
                    winningBoard = searchWinningBoard(tempBoards, calls[counter])
                    if not winningBoard == []:
                        tempBoards.remove(winningBoard)

        counter+=1

    # print(boards)
    print(boards)
    print(tempBoards)
    print(winningBoard)

def getSumOfUnmarkedNums(winningBoard):
    sum = 0
    print(winningBoard)
    for i in range(0, len(winningBoard)):
        for j in range(0, len(winningBoard[i])):
            if not winningBoard[i][j] == "X":

                sum+=int(winningBoard[i][j])

    return sum

def searchWinningBoard(boards, call):
    # loop through boards
    for i in range(0, len(boards)):
        # loop through board row
        for j in range(0, len(boards[i])):

            if boards[i][j].count("X") == len(boards[i][j]):
                # print(getSumOfUnmarkedNums(boards[i]))
                # print(call)
                return boards[i]

            column = []

            for k in range(0, len(boards[i][j])):
                column.append(boards[i][k][j])

            if column.count("X") == len(column):
                # print(getSumOfUnmarkedNums(boards[i]))
                return boards[i]

    return []

def getBoards(boards_raw):
    boards = []
    counter = 0

    # loop through file
    for i in range(0, len(boards_raw)):
        # sanitize string and convert to list
        boardRow = boards_raw[i].strip().split()

        if i == 0: # init board list
            board = [None] * (len(boardRow))

        if boardRow:
            board[counter] = boardRow
            counter+=1

            if counter == len(board):
                boards.append(board) # add board to list of all boards
                board = [None] * (len(boardRow))
                counter = 0

    return boards

main()
