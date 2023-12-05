
def condition(red, green, blue):
    maxRed = 12
    maxGreen = 13
    maxBlue = 14
    if red <=maxRed and green <= maxGreen and blue <= maxBlue:
        return True
    else:
        return False  



def getRedGreenBlue(line):
    red = 0
    green = 0
    blue = 0
    sets = line.strip().split(";")
    for set in sets:
        cubes = set.split(",")
        for cube in cubes:
            valueColor = cube.strip().split()
            value = int(valueColor[0])
            color = valueColor[1]
            match str(color) :
                case "red":
                    red = value
                case "green":
                    green = value
                case "blue":
                    blue = value
                case _:
                    raise TypeError("wrong cube")
    return (red, green, blue)


def getSetPower(sets):
    r = 1
    g = 1
    b = 1
    for set in sets:
        rSet, gSet, bSet = getRedGreenBlue(set)
        if rSet > r:
            r = rSet
        if gSet > g:
            g = gSet
        if bSet > b:
            b = bSet
        
    return r * g * b


def day2(input):
    result = 0
    for line in input:
        splits = line.split(":")
        gameId = int(splits[0].replace("Game ", ""))
        sets = splits[1].split(";")
        setPower =  getSetPower(sets)
        result = result + setPower
    return result



