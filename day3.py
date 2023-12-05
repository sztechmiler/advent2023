
def run(input):
    gearOne = {}
    partsIndexes = []
    lineNo = 0
    result = 0
    for line in input:
        line = line.strip()
        for i in range(len(line)):
            if line[i] == "*":
                
                partsIndexes.append((lineNo-1, i-1))
                partsIndexes.append((lineNo-1, i))
                partsIndexes.append((lineNo-1, i+1))
                partsIndexes.append((lineNo, i-1))
                partsIndexes.append((lineNo, i))
                partsIndexes.append((lineNo, i+1))
                partsIndexes.append((lineNo+1, i-1))
                partsIndexes.append((lineNo+1, i))
                partsIndexes.append((lineNo+1, i+1))
        lineNo = lineNo + 1
    
    lineNo = 0
    i = 0
    for line in input: 
        line = line.strip()
        currStr = ""
        isEngine = False
        for i in range(len(line)): #jeżeli jest liczbą to: sprawdź czy to jest cześć + sprwadź co to za liczba
            if IsNumber(line[i]):
                currStr = currStr + line[i]
                if (lineNo, i) in partsIndexes:
                    isEngine = True
            else: # line[i] == "." or i == len(line) - 1
                if isEngine and currStr != "":
                    result = result + int(currStr)
                    currStr = ""
                    isEngine = False
                currStr = ""
            if i == len(line) -1 and currStr != "" and isEngine == True:
                result = result + int(currStr)
        currStr = ""
        isEngine = False
        lineNo = lineNo + 1

    print(result)
    
def IsNumber(input):
    return str(input).isdigit()


        

        
def run2(input):
    result = 0
    matrix = getMatrix(input)
    matrix_stars = {key: value for key, value in matrix.items() if value == "*"}
    for i, j in matrix_stars.keys():
        result = result + getGearRatio(i, j, matrix)
    print(result)
        
        
        
def getGearRatio(i, j, matrix):
    noOfHits = 0
    valueOne = 1
    indexes = []
    surroundig = getSurroundings(i, j, matrix)
    for v in surroundig:
        if(isinstance(v, Part)):
            index = v.index
            value = v.value
            if index in indexes:
                continue
            indexes.append(index)
            noOfHits = noOfHits + 1
            valueOne = valueOne * value
            if len(indexes) > 2:
                return 0
    if len(indexes) == 2:
        return valueOne
    else:
        return 0
            
        
def getSurroundings(i, j, matrix):
    return [
            matrix[i-1, j-1],
            matrix[i-1, j],
            matrix[i-1, j+1],
            matrix[i, j-1],
            matrix[i, j+1],
            matrix[i+1, j-1],
            matrix[i+1, j],
            matrix[i+1, j+1]
            ]
        
        
    
    
    
    
    
    
    
    return 123
    
def getMatrix(input):
    lineNo = 0
    matrix = {}
    index = 0
    for line in input:
        line = line.strip()
        isNewLine = True
        prevWasNum = False
        for j in range(len(line)):
            value = input[lineNo][j]
            if IsNumber(value):
                if prevWasNum and not isNewLine:
                    part = matrix[(lineNo, j-1)]
                    part.appendVal(value)
                else:
                    index = index + 1
                    part = Part(value, index)
                matrix[(lineNo, j)] = part
                prevWasNum = True
            else:
                prevWasNum = False
                matrix[(lineNo, j)] =  value
            isNewLine = False
        
        lineNo = lineNo + 1
    return matrix


class Part:
    def __init__(self, val, index):
        self.index = index
        self.value = int(val)
    
    def appendVal(self, value):
        strVal = int(str(self.value) + str(value))
        self.value = int(strVal)
        
        
        