#Name:  Jimmy Wu



# part 1
"""def extractDistrict(f):  
    gammaString = ""
    epString = ""
    gamma = 0
    ep = 0
    
    words = f.read().splitlines()
    f.close()
    for index in range(0, len(words[0])):
       
        zeroCount = 0
        oneCount = 0
        for x in words:
            print(x[index])
            if x[index] == '0':
                zeroCount += 1
            else: 
                oneCount += 1
            gamma += 1
        if zeroCount > oneCount:
            gammaString += "0"
            epString += "1"
        else:
            gammaString += "1"
            epString += "0"
            
    print(int(gammaString, 2)*int(epString, 2))

    """
    


# part 2

f = open("day3.txt", "r")
words = f.read().splitlines()
words2 = words
f.close()

counter = 0
counter2 = 0

length = len(words[0])

def co2Scrubber(words, counter):  

    print("done")
    print(words)
    if len(words) == 1:
        return int(words[0], 2)
    else:
        zeroCount = 0
        oneCount = 0
        newListz = []
        newListo = []
        for x in words:
            
            if x[counter] == '0':
                zeroCount += 1
                newListz.append(x)
            else: 
                oneCount += 1
                newListo.append(x)
        if zeroCount <= oneCount:
           
            return co2Scrubber(newListz, counter+1)
            
        else: 
            return co2Scrubber(newListo, counter+1)
    

def oxygenGenerator(words, counter, gammaString):  
    newString = gammaString
    newWords = words

    if not words:
        return int(gammaString, 2)
    elif counter >= length:
        return int(gammaString, 2)
    else:
        zeroCount = 0
        oneCount = 0
        newListz = []
        newListo = []
        for x in words:
            
            if x[counter] == '0':
                zeroCount += 1
                newListz.append(x)
            else: 
                oneCount += 1
                newListo.append(x)
        if oneCount >= zeroCount:
            newString += "1"
            return oxygenGenerator(newListo, counter+1, newString)
        else: 
            prefix = ('0')
            return oxygenGenerator(newListz, counter+1, newString)
    


oner = oxygenGenerator(words,counter,"")
twoer = co2Scrubber(words2,counter2)
print(oner*twoer)


















