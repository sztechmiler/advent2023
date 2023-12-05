import re
        
class Card:
    def __init__(self, id):
        self.cards = []
        self.id = id
        self.numOfMe = 1
    
    def addCards(self, cards):
        self.cards.extend(cards)
    
    def updateMe(self):
        self.numOfMe = self.numOfMe + 1
         
       
def GetCreateCard(key, cardDict: {}) -> Card:
    key = str(key)
    if key in cardDict:
        card = cardDict[key]
        card.updateMe()
        return card
    else:
        card = Card(key)
        cardDict[key] = card
        return card
    
 
def run(input):
    result = 0
    lineNo = 1
    pattern = r"^Card\s+\d+:\s+"
    for line in input:
        card  = re.sub(pattern, '', line)
        numbersStr = card.split("|")
        winningNumbers = getNumbers(numbersStr[0])
        myNumbers = getNumbers(numbersStr[1])
        gamePoint = getGamePoints(winningNumbers, myNumbers)
        result = result + gamePoint
        lineNo = lineNo + 1
    return result

def run2(input):
    result = 1
    lineNo = 1
    cardNo = 1
    maxLineNo = 1
    pattern = r"^Card\s+\d+:\s+"
    cardsDict = {}
    cardsWithCards = {}
    resultDict = {}
    for line in input:
        card  = re.sub(pattern, '', line)
        numbersStr = card.split("|")
        currCard = GetCreateCard(cardNo, cardsDict)
        winningNumbers = getNumbers(numbersStr[0])
        myNumbers = getNumbers(numbersStr[1])
        numOfNextCards = getNumOfNextCards(winningNumbers, myNumbers)
        newCards = GetCards(range(cardNo +1, cardNo + 1 + numOfNextCards), cardsDict)
        currCard.addCards(newCards)
        cardsWithCards[cardNo] = list(range(cardNo +1, cardNo + 1 + numOfNextCards))
        cardNo = cardNo + 1
    finalResult = 0
    for curCardNo in range(1, cardNo):
        result = 1
        for x in range(1, curCardNo + 1):
            if curCardNo in cardsWithCards[x]:
                result = result + resultDict[x]
            resultDict[curCardNo] = result
            
    for a in resultDict.values():
        finalResult = finalResult + a
            
        
            
            
            
        
    return finalResult



    
    
def GetCards(r: range, cardDict: {}):
    result = []
    for i in r:
        result.append(GetCreateCard(str(i), cardDict))
    return result


    
    
def getNumOfNextCards(winningNumbers, myNumbers):
    points = 0
    for myNum in myNumbers:
        if(myNum in winningNumbers):
           points = points + 1
    return points

def getGamePoints(winningNumbers, myNumbers):
    points = 0
    for myNum in myNumbers:
        if(myNum in winningNumbers):
            if points == 0:
                points = 1
            else:
                points = 2 * points
    return points
            
        
def getNumbers(input):
    input = str(input)
    input = input.strip()
    input = re.sub(' +', ' ', input)
    numStr = input.split(" ")
    result = []
    for num in numStr:
        result.append(int(num.strip()))
    return result
    