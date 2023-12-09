def run(input: str):
    instruction = ""
    items = {}
    for line in input:
        if instruction == "":
            instruction = line.strip()
            continue
        if line.strip() == "":
            continue
        splitLine = line.split("=")
        lr = splitLine[1].split(",")
        key = splitLine[0].strip()
        l = lr[0].replace("(", "").replace(")", "").strip()
        r = lr[1].replace("(", "").replace(")", "").strip()
        items[key] = [l, r]
        
    currItem1 = "AAA"
    currItem2 = "NJA"
    currItem3 = "BHA"
    currItem4 = "HTA"
    currItem5 = "LJA"
    currItem6 = "XXA"
    steps = 0
    instructionIndex = 0
    shallGo = True
    while shallGo:
        # print(currItem + "> " + items[currItem][0] +":"+ items[currItem][1])
        currItem1 = items[currItem1][0] if instruction[instructionIndex] == "L" else items[currItem1][1]
        currItem2 = items[currItem2][0] if instruction[instructionIndex] == "L" else items[currItem2][1]
        currItem3 = items[currItem3][0] if instruction[instructionIndex] == "L" else items[currItem3][1]
        currItem4 = items[currItem4][0] if instruction[instructionIndex] == "L" else items[currItem4][1]
        currItem5 = items[currItem5][0] if instruction[instructionIndex] == "L" else items[currItem5][1]
        currItem6 = items[currItem6][0] if instruction[instructionIndex] == "L" else items[currItem6][1]
        steps+=1
        if instructionIndex == len(instruction) -1:
            instructionIndex = 0
        else:
            instructionIndex+=1
        if currItem1[2] == "Z" and currItem2[2] == "Z" and currItem3[2] == "Z" and currItem4[2] == "Z" and currItem5[2] == "Z" and currItem6[2] == "Z":
            shallGo = False
    print(steps)
            