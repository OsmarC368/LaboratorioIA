import random
from .GraphModel import *
import math

grafoIni = {
    "A": { "B": 15, "D": 8, "F":12 },
    "B": { "A": 15, "D": 7, "F": 13, "E": 9, "C": 13 },
    "C": { "B": 13, "E": 9, "F": 16 },
    "D": { "A": 8, "B": 7, "F": 7, "E": 8 },
    "E": { "C": 9, "B": 9, "D": 8, "F":  7},
    "F": { "A": 12, "D": 7, "B": 13, "E": 7, "C": 16 }
}

def permut(tabuList, path):
    while(path in tabuList and len(tabuList) != math.factorial(len(path)-2)):
        ranIndex1 = random.randint(1,len(path)-2)
        ranIndex2 = random.randint(1,len(path)-2)
        while(ranIndex1 == ranIndex2):
            ranIndex2 = random.randint(1,len(path)-2)

        aux = path[ranIndex1]
        path[ranIndex1] = path[ranIndex2]
        path[ranIndex2] = aux

    tabuList.append(path.copy())
    return path, tabuList

def solve(initSolv):
    tabuList = []
    minVal = count(initSolv, grafoIni)
    minPath = initSolv.copy()

    for _ in range(math.factorial(len(initSolv)-2)):
        sol, tabuList = permut(tabuList, initSolv)
        try:
            newCount = count(sol, grafoIni)
            if newCount < minVal:
                minVal = newCount
                minPath = sol
        except:
            continue
        initSolv = sol.copy()

    print(minPath)
    print(minVal)
    return [minPath, minVal], tabuList, grafoIni

# solve("A-B-C-E-F-D-A".split("-"))