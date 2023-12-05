import re


def run():
    seeds = "79 14 55 13"
    seedToSoilMap = """50 98 2
    52 50 48"""

    soilToFertilizerMap = """0 15 37
37 52 2
39 0 15"""
    fertilizerToWaterMap = """49 53 8
0 11 42
42 0 7
57 7 4"""
    waterToLightMap = """88 18 7
18 25 70"""
    ligthToTemperatureMap = """45 77 23
81 45 19
68 64 13"""
    tempartureToHumidityMap = """0 69 1
1 0 69"""
    humidityToLocationMap = """60 56 37
56 93 4"""
    
    seeds = re.findall(r'\d+', seeds)
    seedToSoil = [list(map(int, line.split())) for line in seedToSoilMap.split('\n')]
    soilToFertilizer = [list(map(int, line.split())) for line in soilToFertilizerMap.split('\n')]
    fertilizerToWater = [list(map(int, line.split())) for line in fertilizerToWaterMap.split('\n')]
    waterToLight = [list(map(int, line.split())) for line in waterToLightMap.split('\n')]
    ligthToTemperature = [list(map(int, line.split())) for line in ligthToTemperatureMap.split('\n')]
    tempartureToHumidity = [list(map(int, line.split())) for line in tempartureToHumidityMap.split('\n')]
    humidityToLocation = [list(map(int, line.split())) for line in humidityToLocationMap.split('\n')]
    
    lowest = 33366006921 
    startSeed = 0
    endSeed = 0
    # for index, item in enumerate(seeds):
    for i in range(0, len(seeds), 2):
        seedStart = int(seeds[i])
        seedend = seedStart +  int(seeds[i+1]) - 1
        seedList = [[seedStart, seedend]]
        soilList = getNewNumber(seedList, seedToSoil)
        fertiList = getNewNumber(soilList, soilToFertilizer)
        waterList = getNewNumber(fertiList, fertilizerToWater)
        lightList = getNewNumber(waterList, waterToLight)
        tempList = getNewNumber(lightList, ligthToTemperature)
        humiList = getNewNumber(tempList, tempartureToHumidity)
        locList = getNewNumber(humiList, humidityToLocation)
        smallest_first_item = min(sublist[0] for sublist in locList)
        if smallest_first_item < lowest:
            lowest = smallest_first_item
    return lowest
        
        

def getNewNumber(seedDataList: list, maps: list) -> list:
    result = []
    changed = seedDataList[:]
    for map in maps:
        seedDataList = changed[:]
        changed = []
        while len(seedDataList) > 0:
            seedData = seedDataList.pop(0)
            for i in range(0, len(seedData), 2):
                seedStart = int(seedData[i])
                seedEnd = int(seedData[i+1])
                destStart = map[0]
                sourceStart = map[1]
                destEnd = destStart + map[2] - 1
                sourceEnd = sourceStart + map[2] - 1
                move = destStart - sourceStart 
                
                if sourceStart > seedEnd or sourceEnd < seedStart:
                    changed.append([seedStart, seedEnd])
                elif sourceStart <= seedStart and sourceEnd >= seedEnd: 
                    result.append([seedStart + move, seedEnd + move])
                elif sourceStart <= seedStart:
                    result.append([seedStart+move, sourceEnd + move])
                    changed.append([min(sourceEnd + 1, seedEnd), seedEnd])
                elif sourceEnd <= seedEnd:
                    changed.append([seedStart, sourceStart -1])
                    result.append([sourceEnd + move, seedEnd + move])
                else:
                    changed.append([seedStart, sourceStart - 1])
                    result.append([sourceStart + move, sourceEnd + move])
                    changed.append([min(sourceEnd + 1, seedEnd), seedEnd])
    result.extend(changed)
    return result


def getNewNumber2(seed:int, maps: list) -> int:
    for map in maps:
        destStart = map[0]
        sourceSart = map[1]
        destEnd = destStart + map[2] - 1
        sourceEnd = sourceSart + map[2] - 1
        move = destStart - sourceSart 
        if seed >= sourceSart and seed <= sourceEnd:
            seed = seed + move
            return seed
    return seed
        