#Name:  Jimmy Wu

f = open("day4.txt", "r")
text = f.read().splitlines()

f.close()

bingoArray = []
binNums = []
bingoDict = {}

i = 0
for x in text:
    if len(x) == 14:
        bingoArray.append(x.split())
    elif len(x) > 14:
        binNums = x.split(",")
    

print(binNums) 


#Day 4 part 1 code:
#only horizontal and vertical
def bingoDay4Part1(bingoArray, binNums):
    #list of all called bingo numbers
    bingoNums = []
    for b in binNums:
        bingoNums.append(b)
        for i in range(len(bingoArray)):
            for j in range(len(bingoArray[i])):
                
                rowBingo = 0
                for x in bingoArray[i]:
                    if x in bingoNums:
                        rowBingo += 1
                    if rowBingo == 5:
                        boardNum = i/5
                        
                        

                        print(bingoNums)
                        
                        #return("BINGO at board: " + str(boardNum+1))
                        scoreJustCalled = int(bingoNums[-1])
                        rowNum = i - i%5
                        return(scoreJustCalled*getUnmarkedNumsSum(rowNum, bingoNums))
                
                if i%5 == 0:
                    if (i+4 < len(bingoArray)):
                        boardNum = i/5
                        
                        #vertical checking
                        if bingoArray[i][j] in bingoNums and bingoArray[i+1][j] in bingoNums and bingoArray[i+2][j] in bingoNums and bingoArray[i+3][j] in bingoNums and bingoArray[i+4][j] in bingoNums:
                            """
                            
                            print(bingoArray[i][j]+bingoArray[i+1][j]+bingoArray[i+2][j]+bingoArray[i+3][j]+bingoArray[i+4][j])

                            """
                            print(bingoNums)
                            scoreJustCalled = int(bingoNums[-1])
                            rowNum = i - i%5 
                            return(scoreJustCalled*getUnmarkedNumsSum(rowNum, bingoNums))
                        
                    
#Day 4 part 2 code: recursively remove completed boards until only 1 is left
#only horizontal and vertical 
#unfortunately very slow if a lot of boards
numOfBoards = len(bingoArray)/5

#list of all called bingo numbers
bingoNums = []

def bingoDay4Part2(bingoArray, binNums, numOfBoards, scoreJustCalled, bingoNums2):
    print(str(numOfBoards) + " boards left")
    bingoNums = bingoNums2.copy()
    newBingoArray = bingoArray.copy()
   
    if(numOfBoards <= 0):
        return scoreJustCalled*getUnmarkedNumsSumLastBoard(bingoNums, newBingoArray)
    
    
    
    for b in binNums:
        
        #may rewrite code so bingoNums gets appended after checking through all boards. As it is right now, if multiple boards get bingoed at the same time, it will remove the first board and then add another bingo num to bingoNums, thus when the next board is removed, the last num to be called will be different even tho the boards were bingoed at the same time
        bingoNums.append(b)
        for i in range(len(bingoArray)):
            for j in range(len(bingoArray[i])):
                
                rowBingo = 0
                for x in bingoArray[i]:
                    if x in bingoNums:
                        rowBingo += 1
                    if rowBingo == 5:
                        boardNum = i/5
                        rowNum = i - i%5 
                        
                        scoreJustCalled = int(bingoNums[-1])
                        
                        
                        if numOfBoards == 1:
                            return bingoDay4Part2(newBingoArray, binNums,numOfBoards-1, scoreJustCalled, bingoNums)
                            
                        
                        k = 0
                        while k < 5:
                            newBingoArray.pop(rowNum)
                            k += 1
                      
                      
                        
                        
                        return bingoDay4Part2(newBingoArray, binNums,numOfBoards-1, scoreJustCalled, bingoNums)
                        
                      
                
                if i%5 == 0:
                    if (i+4 < len(bingoArray)):
                        boardNum = i/5
                        
                        #vertical checking
                        if bingoArray[i][j] in bingoNums and bingoArray[i+1][j] in bingoNums and bingoArray[i+2][j] in bingoNums and bingoArray[i+3][j] in bingoNums and bingoArray[i+4][j] in bingoNums:
                            """
                            
                            print(bingoArray[i][j]+bingoArray[i+1][j]+bingoArray[i+2][j]+bingoArray[i+3][j]+bingoArray[i+4][j])

                            """
                            rowNum = i - i%5
                            scoreJustCalled = int(bingoNums[-1])
                            
                            
                            if numOfBoards == 1:
                                return bingoDay4Part2(newBingoArray, binNums,numOfBoards-1, scoreJustCalled, bingoNums)
                        
                            k = 0
                            while k < 5:
                                newBingoArray.pop(rowNum)
                                k += 1
                      
                                
     
                            
                            return bingoDay4Part2(newBingoArray, binNums,numOfBoards-1, scoreJustCalled, bingoNums)
                            
                            
                        
                    


def getUnmarkedNumsSum(winningBoardFirstRow, bingoNums):
    uniqueBingoNums = list(set(bingoNums))
    print(uniqueBingoNums)
    print(winningBoardFirstRow)
    counter = int(winningBoardFirstRow)
    unmarkedNumsSum = 0
    winningBoard = []
    print("WINNING BOARD:")
    for i in range(counter, counter+5):
        print(bingoArray[i])
        for j in range(len(bingoArray[i])):
            unmarkedNumsSum += int(bingoArray[i][j])
            winningBoard.append(int(bingoArray[i][j]))
    for x in uniqueBingoNums:
        if int(x) in winningBoard:
            unmarkedNumsSum -= int(x)
    return(unmarkedNumsSum)

def getUnmarkedNumsSumLastBoard(bingoNums, newBingoArray):

    uniqueBingoNums = list(set(bingoNums))
    print(uniqueBingoNums)
   
    counter = 0
    unmarkedNumsSum = 0
    winningBoard = []
    print("WINNING BOARD:")
    for i in range(counter, counter+5):
        print(newBingoArray[i])
        for j in range(len(newBingoArray [i])):
            unmarkedNumsSum += int(newBingoArray[i][j])
            winningBoard.append(int(newBingoArray[i][j]))
            
    for x in uniqueBingoNums:
        if int(x) in winningBoard:
            unmarkedNumsSum -= int(x)
    
    return(unmarkedNumsSum)
        




#print(bingoDay4Part1(bingoArray,binNums))
print(bingoDay4Part2(bingoArray,binNums,numOfBoards, 0, []))
    




    
#testing code ####################################################################
def bingoTestingMethod(bingoArray):
    counter = 0
    for i in range(len(bingoArray)):
        for j in range(len(bingoArray[i])):
            
            #checks each row for bingo
            rowBingo = 0
            for x in bingoArray[i]:
                if x in binNums:
                    rowBingo += 1
                if rowBingo == 5:
                    print("BINGO at: " + str(i+1))
                    print(x)
    
                    
            #only checking every 5 rows or every bingo board for verticals and diagonals
            if i%5 == 0:
                
                #check if out of bounds for i first
                if (i+4 < len(bingoArray)):
                    boardNum = i/5
                    #checks vertical first
                    if bingoArray[i][j] in binNums and bingoArray[i+1][j] in binNums and bingoArray[i+2][j] in binNums and bingoArray[i+3][j] in binNums and bingoArray[i+4][j] in binNums:
                        print("BINGO at: " + str(boardNum+1))
                        print(bingoArray[i][j]+bingoArray[i+1][j]+bingoArray[i+2][j]+bingoArray[i+3][j]+bingoArray[i+4][j])
                    
                    if j == 0 and bingoArray[i][j] in binNums and bingoArray[i+1][j+1] in binNums and bingoArray[i+2][j+2] in binNums and bingoArray[i+3][j+3] in binNums and bingoArray[i+4][j+4] in binNums:
                        print("BINGO at: " + str(boardNum+1))
                        print(bingoArray[i][j]+bingoArray[i+1][j+1]+bingoArray[i+2][j+2]+bingoArray[i+3][j+3]+bingoArray[i+4][j+4])
                    elif j == 4 and bingoArray[i][j] in binNums and bingoArray[i+1][j-1] in binNums and bingoArray[i+2][j-2] in binNums and bingoArray[i+3][j-3] in binNums and bingoArray[i+4][j-4] in binNums:
                       
                        print("BINGO at: " + str(boardNum+1))
                        print(bingoArray[i][j] + bingoArray[i+1][j-1] + bingoArray[i+2][j-2] +  bingoArray[i+3][j-3] +  bingoArray[i+4][j-4])

    for x in bingoArray:
        print(x)


#This works with diagonals and vertical/horizontal
def bingoTestingMethod2(bingoArray, binNums):
    bingoNums = []
    for b in binNums:
        bingoNums.append(b)
        print(bingoNums)
        for i in range(len(bingoArray)):
            for j in range(len(bingoArray[i])):
                
                rowBingo = 0
                for x in bingoArray[i]:
                    if x in bingoNums:
                        rowBingo += 1
                    if rowBingo == 5:
                        boardNum = i/5
                        print(bingoArray[i])
                        return("BINGO at board: " + str(boardNum+1))
                
                if i%5 == 0:
                    if (i+4 < len(bingoArray)):
                        boardNum = i/5
                        
                        #vertical checking
                        if bingoArray[i][j] in bingoNums and bingoArray[i+1][j] in bingoNums and bingoArray[i+2][j] in bingoNums and bingoArray[i+3][j] in bingoNums and bingoArray[i+4][j] in bingoNums:
                            
                            print(bingoArray[i][j]+bingoArray[i+1][j]+bingoArray[i+2][j]+bingoArray[i+3][j]+bingoArray[i+4][j])
                            return("BINGO at: " + str(boardNum+1))
                        
                        
                        #diagonal checking from top left to bottom right
                        if j == 0 and bingoArray[i][j] in bingoNums and bingoArray[i+1][j+1] in bingoNums and bingoArray[i+2][j+2] in bingoNums and bingoArray[i+3][j+3] in bingoNums and bingoArray[i+4][j+4] in bingoNums:
     
                            print(bingoArray[i][j]+bingoArray[i+1][j+1]+bingoArray[i+2][j+2]+bingoArray[i+3][j+3]+bingoArray[i+4][j+4])
                            return("BINGO at: " + str(boardNum+1))
                        
                        #diagonal checking from top right to bottom left
                        elif j == 4 and bingoArray[i][j] in bingoNums and bingoArray[i+1][j-1] in bingoNums and bingoArray[i+2][j-2] in bingoNums and bingoArray[i+3][j-3] in bingoNums and bingoArray[i+4][j-4] in bingoNums:
                       
                            
                            print(bingoArray[i][j] + bingoArray[i+1][j-1] + bingoArray[i+2][j-2] +  bingoArray[i+3][j-3] +  bingoArray[i+4][j-4])
                            return("BINGO at: " + str(boardNum+1))
                
    for x in bingoArray:
        print(x)
    



     