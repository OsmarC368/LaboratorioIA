from tabulate import tabulate
import random
from QueenModel import *
from math import *

def permut(list, tabuList):
    while(list in tabuList and len(tabuList) != 24):
        ranIndex1 = random.randint(0,len(list)-1)
        ranIndex2 = random.randint(0,len(list)-1)
        while(ranIndex1 == ranIndex2):
            ranIndex2 = random.randint(0,len(list)-1)

        aux = list[ranIndex1]
        list[ranIndex1] = list[ranIndex2]
        list[ranIndex2] = aux

    tabuList.append(list.copy())
    return list, tabuList

def solve():
    initialSol = [1,2,3,4,5,6,7,8,9]
    tabuList = []
    colMin = countColisions(createTable(initialSol), initialSol)
    sol2 = []
    while(1 > 0):
        sol, tabuList = permut(initialSol, tabuList)
        newCol = countColisions(createTable(sol), sol)


        if len(tabuList) == factorial(len(initialSol)):
            break
        elif colMin > newCol:
            sol2 = sol
            colMin = countColisions(createTable(sol), sol)
        
        if newCol == 0:
            sol2 = sol
            break
    
    print(f"Numero de Colisiones: {countColisions(createTable(sol2), sol2)}")
    print(tabulate(createTable(sol2), tablefmt="fancy_grid"))

solve()