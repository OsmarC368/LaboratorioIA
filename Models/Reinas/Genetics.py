from .QueenModel import *
import random
from tabulate import tabulate

def generateTable(numGen, qList):
    Fi = sum([countColisions(createTable(placement), placement) for placement in qList])
    table = []
    totalPerc = 0
    acumProb = 0
    for i, num in enumerate(qList):
        aux = [[x for x in num]]
        col = countColisions(createTable(num), num)
        acumProb += col / Fi
        aux.append(col)
        aux.append(format((col / Fi),".2f"))
        aux.append(format(acumProb,".2f"))
        table.append(aux)
        totalPerc += col / Fi

    table.append(["Total",Fi,totalPerc, acumProb])
    print(f"\n/------------------------- Gen #{numGen} -------------------------/")
    print(tabulate(table, headers=["Reinas", "fitness", "Probabilidad", "Probabilidad Acumulada"], tablefmt="fancy_grid"))
    return table[:-1]
    
def mutar(placement, qNum):
    ind = placement[0][0:qNum]
    ranIndex1 = random.randint(0, len(ind)-1)
    ranIndex2 = random.randint(0, len(ind)-1)
    while(ranIndex1 == ranIndex2):
        ranIndex2 = random.randint(0, len(ind)-1)

    aux = ind[ranIndex1]
    ind[ranIndex1] = ind[ranIndex2]
    ind[ranIndex2] = aux

    return [ind]


def tournament(table):
    ran1 = random.randint(0,len(table)-1)
    ran2 = random.randint(0,len(table)-1)
    while(ran1 == ran2):
        ran2 = random.randint(0,len(table)-1)
    
    if table[ran1][1] < table[ran2][1] or table[ran1][1] == table[ran2][1]:
        return table[ran1]
    elif table[ran2][1] < table[ran1][1]:
        return table[ran2]

def path(num, table, qNum):

    if num[1] == 0:
        return num
    elif random.random() > 0.1:
        return cruzar(num, table, qNum)
        #return num[2]
    else:
        return mutar(num, qNum)

def cruzar(num, table, qNum):

    ranNum = tournament(table)

    permut1 = num[0]
    permut2 = ranNum[0]

    c1 = int(len(permut1) / 3)
    c2 = len(permut1) - c1
    
    #Ahora hacemos los hijos con Arms y Core
    #Cores
    childCore1 = permut2[c1:c2]
    childCore2 = permut1[c1:c2]
    
    #CHILD 1
    #Arms
    arm1 = []
    for x in permut1[0:c1]:
        if x not in childCore1:
            arm1.append(x)
        else:
            arm1.append(0)

    arm2 = []
    for x in permut1[c2:]:
        if x not in childCore1:
            arm2.append(x)
        else:
            arm2.append(0)

    child1 = arm1 + childCore1 + arm2
    
    for i,x in enumerate(child1):
        if x == 0:
            for z in range(qNum):
                if z+1 not in child1:
                    child1[i] = z+1
                    break

    #CHILD 2
    arm21 = []
    for x in permut2[0:c1]:
        if x not in childCore2:
            arm21.append(x)
        else:
            arm21.append(0)

    arm22 = []
    for x in permut2[c2:]:
        if x not in childCore2:
            arm22.append(x)
        else:
            arm22.append(0)

    child2 = arm21 + childCore2 + arm22
    
    for i,x in enumerate(child2):
        if x == 0:
            for z in range(qNum):
                if z+1 not in child2:
                    child2[i] = z+1
                    break

    return [child1, child2]

def genInitialSol(qNum, indNum):
    numList = []
    while(len(numList) < indNum):
        aux = []
        while(len(aux) < qNum):
            ranNum = random.randint(1,qNum)
            if not ranNum in aux:
                aux.append(ranNum)
        numList.append(aux)
    return numList

def solve(indNum, qNum, genNum):
    numList = genInitialSol(qNum, indNum)
    val = True
    numGen = 1
    finalAns = None
    while(numGen < genNum and val):
        table = generateTable(numGen, numList)
        for x in numList:
            if countColisions(createTable(x), x) == 0:
                print(f"\n/----------Se Encontro una Solucion Perfecta! en la Gen#{numGen}----------------/")
                print(tabulate(createTable(x), tablefmt="fancy_grid"))
                print(f"Colisiones: {countColisions(createTable(x), x)}\n")
                val = False
                finalAns = [x, countColisions(createTable(x), x)]
                break
        
        newGen = []
        while len(newGen) < indNum:
            # result = path(ruleta(table[::-1]), table, len(numList[0]))
            result = path(tournament(table), table, len(numList[0]))
            for ind in result:
                if len(newGen) < indNum:
                    newGen.append(ind)
        numList = newGen.copy()
        numGen += 1
    return finalAns, table