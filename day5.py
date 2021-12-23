
def day5(txtName, partNum):
    textFile = open(txtName, "r")
    text = textFile.read().splitlines()
    textFile.close()
    
    graphDiagramDict = {}
    
    for p in text:
        pair = p.split(' -> ')
        firstPoint = [int(f) for f in pair[0].split(',')]
        secondPoint = [int(f) for f in pair[1].split(',')]
        
        isLine = False
        
        #horizontal and vertical

        #check x values of pair
        if firstPoint[0] == secondPoint[0]:
            isLine = True
            
            #add the points in between the 2 pairs
            if firstPoint[1] > secondPoint[1] and (firstPoint[1] - secondPoint[1]) > 1 :
                for newY in range(secondPoint[1]+1,firstPoint[1]):
                    checkIfPointExists(tuple([firstPoint[0],newY]), graphDiagramDict)
            elif secondPoint[1] > firstPoint[1] and (secondPoint[1] - firstPoint[1]) > 1 :
                for newY in range(firstPoint[1]+1,secondPoint[1]):
                    checkIfPointExists(tuple([firstPoint[0],newY]), graphDiagramDict)
                
    
        #check y values of pair 
        elif firstPoint[1] == secondPoint[1]:
            isLine = True
            #add the points in between the 2 pairs
            if firstPoint[0] > secondPoint[0] and (firstPoint[0] - secondPoint[0]) > 1:
                for newX in range(secondPoint[0]+1,firstPoint[0]):
                    checkIfPointExists(tuple([newX,firstPoint[1]]), graphDiagramDict)
            elif secondPoint[0] > firstPoint[0] and (secondPoint[0] - firstPoint[0]) > 1 :
                for newX in range(firstPoint[0]+1,secondPoint[0]):
                    checkIfPointExists(tuple([newX,firstPoint[1]]), graphDiagramDict)
                
            
    
        
   
        #Part 2
        #Checks for diagonals
        if partNum == 2:
            if abs(firstPoint[0] - secondPoint[0]) == abs(firstPoint[1] - secondPoint[1]):
                isLine = True
                
                #Checks if there are points in between the two points
                lengthBetweenPointsX = abs(firstPoint[0] - secondPoint[0])
                if lengthBetweenPointsX > 1:
                
                    #checks if points are like 1,1 -> 4,4 or 0,0 -> 5,5
                    #would add all points in between 
                    if firstPoint[0] == firstPoint[1] and secondPoint[0] == secondPoint[1]:
                        if(firstPoint[0] > secondPoint[0]):
                            for newVals in range(secondPoint[0]+1,firstPoint[0]):
                                checkIfPointExists(tuple([newVals,newVals]), graphDiagramDict)
                        elif(secondPoint[0] > firstPoint[0]):
                            for newVals in range(firstPoint[0]+1,secondPoint[0]):
                                checkIfPointExists(tuple([newVals,newVals]), graphDiagramDict)
                    
                    elif(firstPoint[0] == secondPoint[1] and firstPoint[1] == secondPoint[0]):
                        
                        #if first point's x is greater than its y, that means first point's x is also greater than second point's x
                        if firstPoint[0] > firstPoint[1]:
                            for itr in range(1,lengthBetweenPointsX):
                                checkIfPointExists(tuple([firstPoint[0]-itr, firstPoint[1]+itr]), graphDiagramDict)
                        
                        #if firstPoint's y is greater than its x, that means first point's y is also greater than second point's y
                        elif firstPoint[1] > firstPoint[0]:
                            for itr in range(1,lengthBetweenPointsX):
                                checkIfPointExists(tuple([firstPoint[0]+itr, firstPoint[1]-itr]), graphDiagramDict)
                    else:
                        
                        if firstPoint[0] > secondPoint[0]: 
                            if firstPoint[1]>secondPoint[1]:  
                                for itr in range(1,lengthBetweenPointsX): 
                                    checkIfPointExists(tuple([firstPoint[0]-itr, firstPoint[1]-itr]), graphDiagramDict)
                            else: 
                                for itr in range(1,lengthBetweenPointsX):
                                    checkIfPointExists(tuple([firstPoint[0]-itr, firstPoint[1]+itr]), graphDiagramDict)
                       
                        elif firstPoint[0]<secondPoint[0]:
                            if firstPoint[1]<secondPoint[1]:
                                for itr in range(1,lengthBetweenPointsX):
                                    checkIfPointExists(tuple([firstPoint[0]+itr, firstPoint[1]+itr]), graphDiagramDict)
                            else:
                                for itr in range(1,lengthBetweenPointsX):     
                                    checkIfPointExists(tuple([firstPoint[0]+itr, firstPoint[1]-itr]), graphDiagramDict)
                        

        if isLine is True:
            #add the points of the 2 pairs (endpoints of the line)
            checkIfPointExists(firstPoint, graphDiagramDict)
            checkIfPointExists(secondPoint, graphDiagramDict)
                    
                    

    bigCounter = 0
    for x in graphDiagramDict.values():
        if x > 1:
            bigCounter += 1
            
    return(bigCounter)   

            
def checkIfPointExists(pointToCheck, graphToCheck):
    if tuple(pointToCheck) not in graphToCheck.keys():
        graphToCheck[tuple(pointToCheck)] = 1
    else: 
        graphToCheck[tuple(pointToCheck)] += 1
            
print(day5("day5test.txt", 1))    
print(day5("day5test.txt", 2))
    
print(day5("day5.txt", 1))
print(day5("day5.txt", 2))

 