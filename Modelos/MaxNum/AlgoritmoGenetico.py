import random
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as geek

def funcion(x):
    return (x**4) - (4*(x**3)) + (7*x) 

def generateTable(numGen, numList):
    Fi = sum([funcion(x) for x in numList])
    table = []
    totalPerc = 0
    for i, num in enumerate(numList):
        aux = []
        aux.append(i+1)
        aux.append(bin(num)[2:])
        aux.append(num)
        aux.append(funcion(num))
        if Fi == 0:
            aux.append(0)
        else:
            aux.append(format(((funcion(num) / Fi) * 100),".2f"))
        table.append(aux)
        totalPerc += (funcion(num) / Fi) * 100 if Fi != 0 else 0
    table.append(["Total","","",Fi,totalPerc])
    print(f"\n/------------------------- Gen #{numGen} -------------------------/")
    print(tabulate(table, headers=["N", "Población", "X", "fitness", "Porcentaje"], tablefmt="fancy_grid"))
    return table[:-1]
    
def mutar(num, maxRange):
    ranIndex = random.randint(0, len(num[1]) - 1)
    aux = num[2]

    if num[1][0] == "b":
        bin = list(num[1])
        bin[0] = '0'
        return [int("".join(bin), 2)]
    elif num[1][ranIndex] == "1":
        newBin = list(num[1])
        newBin[ranIndex] = "0"
        num[1] = "".join(newBin)
    else:
        newBin = list(num[1])
        newBin[ranIndex] = "1"
        num[1] = "".join(newBin)

    if int(num[1], 2) > maxRange:
        return [aux]
    else:
        return [int(num[1], 2)]

def ruleta(table):
    ranNum = random.random()
    acum = 0
    val = True
    num = 0
    for row in table:
        acum += (float(row[4]) / 100)
        if acum > ranNum:
            num = row
            val = False
            break
    return num if not val else table[-1]

def path(num, table, maxRange):
    if random.random() > 0.1:
        return cruzar(num, table, maxRange)
    else:
        return mutar(num, maxRange)

def cruzar(num, table, maxRange):
    numRan = ruleta(table)

    p1 = list(num[1])
    p2 = list(numRan[1])

    if p1[0] == "b" or p2[0] == "b":
        return [num[2], numRan[2]]
    elif len(p1) == 1 or len(p2) == 1:
        return [int("".join(p1), 2), int("".join(p2), 2)]
    
    minN = len(p1) if len(p1) <= len(p2) else len(p2)

    ranInd1, ranInd2 = random.sample(range(minN), 2)

    aux1 = p1[ranInd1]
    aux2 = p1[ranInd2]
    p1[ranInd1] = p2[ranInd1]
    p1[ranInd2] = p2[ranInd2]
    p2[ranInd1] = aux1
    p2[ranInd2] = aux2


    if int("".join(p1), 2) > maxRange or  int("".join(p2), 2) > maxRange:
        return [num[2]] if num[3] >= numRan[3] else [numRan[2]]
    else:
        return [int("".join(p1), 2), int("".join(p2), 2)]



def solve():
    numList = []
    cicle = 1
    while(len(numList) < 5):
        num = random.randint(-2,4)
        if num not in numList:
            numList.append(num)

    while(cicle != 21):
        newGen = []
        firstTable = generateTable(cicle, numList)
        while(len(newGen) < 5):
            result = path(ruleta(firstTable), firstTable, 4)
            for x in result:
                if len(newGen) < 5:
                    newGen.append(x)
        numList = newGen.copy()
        cicle += 1


def graph(rang, max):
    x = geek.linspace(float(rang[0]), float(rang[1]), num=30)
    # x = geek.arange(rang[0], rang[1], 0.01)
    y = [funcion(z) for z in x]
    plt.plot(x, y)
    plt.grid(True)
    plt.axvline(max, color="green", linestyle="--")
    plt.title("Grafico de la Funcion", loc="center", fontsize=16)
    plt.legend(["Funcion", "Maximo"])
    plt.rc('axes', axisbelow=True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


solve()
graph([-2,4], -2)