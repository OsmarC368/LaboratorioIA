from GraphModel import *
import random
import math

grafoIni = {
    "A": { "B": 15, "D": 8, "F":12 },
    "B": { "A": 15, "D": 7, "F": 13, "E": 9, "C": 13 },
    "C": { "B": 13, "E": 9, "F": 16 },
    "D": { "A": 8, "B": 7, "F": 7, "E": 8 },
    "E": { "C": 9, "B": 9, "D": 8, "F":  7},
    "F": { "A": 12, "D": 7, "B": 13, "E": 7, "C": 16 }
}


def calcRanges(path):
    z = 1 / len(path)
    ranges = []
    for i, x in enumerate(path):
        aux = []
        aux.append(x)
        aux.append((z*i))
        aux.append(z*(i+1))
        ranges.append(aux)
    return ranges

def ranSelection(ranges):
    ranNum = random.random()
    for x in ranges:
        if x[1] < ranNum < x[2]:
            return x[0]

def probAccept(Zc, Zn, T):
    return math.exp(-(Zn - Zc) / T)

def solve(initPath):
    temperatures = []
    bestPath = [initPath, count(initPath, grafoIni)]
    for _ in range(3000):
        #---------------------------------------------------
        if len(temperatures) > 0:
            if temperatures[-1] < 0.1:
                break
        #---------------------------------------------------

        Zc = count(initPath, grafoIni)

        if Zc < bestPath[1]:
            bestPath[0] = initPath.copy()
            bestPath[1] = Zc

        #---------------------------------------------------
        pathAux = initPath.copy()
        ranges = calcRanges(pathAux[1:-2])
        ran1 = ranSelection(ranges)
        ran2 = ranSelection(calcRanges(pathAux[pathAux.index(ran1)+1: -1]))
        aux = pathAux[pathAux.index(ran1)]
        indexAux = pathAux.index(ran2)
        pathAux[pathAux.index(ran1)] = ran2
        pathAux[indexAux] = aux
        #---------------------------------------------------

        try:
            #---------------------------------------------------

            Zn = count(pathAux, grafoIni)

            if len(temperatures) > 0:
                T = temperatures[-1] * 0.9
            else:
                T = 0.6 * Zc
            #---------------------------------------------------

            if Zn < Zc:
                initPath = pathAux.copy()
            else:
                prob = probAccept(Zc, Zn, T)
                if random.random() < prob:
                    initPath = pathAux.copy()
            temperatures.append(T)

            #---------------------------------------------------

        except:
            continue

        
    print("El Mejor Recorrido Encontrado es:")
    print(f"Camino: {bestPath[0]}")
    print(f"Valor del Camino: {bestPath[1]}")

solve("A-B-C-E-F-D-A".split("-"))