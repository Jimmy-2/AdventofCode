



#use dictioanry instead of array to check for duplicate values/intersections later
graphDiagramDict = {}
def day5Part1(txtName):
    textFile = open(txtName, "r")
    text = textFile.read().splitlines()

    textFile.close()

    for p in text:
        pair = p.split(' -> ')
        firstPoint = [int(f) for f in pair[0].split(',')]
        secondPoint = [int(f) for f in pair[1].split(',')]
        
        if firstPoint[0] == secondPoint[0]:
            if firstPoint[1] > secondPoint[1] and (firstPoint[1] - secondPoint[1]) > 1 :
                for newY in range(secondPoint[1]+1,firstPoint[1]):
                    newPoint = [firstPoint[0],newY]
                    if tuple(newPoint) not in graphDiagramDict.keys():
                        graphDiagramDict[tuple(newPoint)] = 1
                    else:
                        graphDiagramDict[tuple(newPoint)] += 1
            elif secondPoint[1] > firstPoint[1] and (secondPoint[1] - firstPoint[1]) > 1 :
                for newY in range(firstPoint[1]+1,secondPoint[1]):
                    newPoint = [firstPoint[0],newY]
                    if tuple(newPoint) not in graphDiagramDict.keys():
                        graphDiagramDict[tuple(newPoint)] = 1
                    else:
                        graphDiagramDict[tuple(newPoint)] += 1
                
                
                
            
            if tuple(firstPoint) not in graphDiagramDict.keys():
                graphDiagramDict[tuple(firstPoint)] = 1
            else: 
                graphDiagramDict[tuple(firstPoint)] += 1
                
                
            if tuple(secondPoint) not in graphDiagramDict.keys():
                graphDiagramDict[tuple(secondPoint)] = 1
            else: 
                graphDiagramDict[tuple(secondPoint)] += 1
           
            #add all points with same x but range y
        elif firstPoint[1] == secondPoint[1]:
            if firstPoint[0] > secondPoint[0] and (firstPoint[0] - secondPoint[0]) > 1 :
                for newX in range(secondPoint[0]+1,firstPoint[0]):
                    newPoint = [newX,firstPoint[1]]
                    if tuple(newPoint) not in graphDiagramDict.keys():
                        graphDiagramDict[tuple(newPoint)] = 1
                    else:
                        graphDiagramDict[tuple(newPoint)] += 1
            elif secondPoint[0] > firstPoint[0] and (secondPoint[0] - firstPoint[0]) > 1 :
                for newX in range(firstPoint[0]+1,secondPoint[0]):
                    newPoint = [newX,firstPoint[1]]
                    if tuple(newPoint) not in graphDiagramDict.keys():
                        graphDiagramDict[tuple(newPoint)] = 1
                    else:
                        graphDiagramDict[tuple(newPoint)] += 1
                
            
            
            
            if tuple(firstPoint) not in graphDiagramDict.keys():
                graphDiagramDict[tuple(firstPoint)] = 1
            else: 
                graphDiagramDict[tuple(firstPoint)] += 1
                
                
            if tuple(secondPoint) not in graphDiagramDict.keys():
                graphDiagramDict[tuple(secondPoint)] = 1
            else: 
                graphDiagramDict[tuple(secondPoint)] += 1
    
    bigCounter = 0
    for x in graphDiagramDict.values():
        if x > 1:
            bigCounter += 1
            
    return(bigCounter)   

            
            
print(day5Part1("day5.txt"))



 