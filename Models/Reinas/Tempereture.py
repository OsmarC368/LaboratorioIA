import random
from .QueenModel import *
from tabulate import tabulate

def permut(list):
    ranIndex1 = random.randint(0,len(list)-1)
    ranIndex2 = random.randint(0,len(list)-1)
    while(ranIndex1 == ranIndex2):
        ranIndex2 = random.randint(0,len(list)-1)

    aux = list[ranIndex1]
    list[ranIndex1] = list[ranIndex2]
    list[ranIndex2] = aux
    return list


def solve(initSol):
    initialSol = {
        "list": initSol,
        "colNum": countColisions(createTable(initSol), initSol) 
        }
    
    colX = initialSol["colNum"]
    itr = 0
    val = True
    while(itr != 3000 and val):
        x = permut(initialSol["list"])
        z = countColisions(createTable(x), x) 
        if  z == 0:
            initialSol["list"] = x
            initialSol["colNum"] = z
            val = False
        elif z < initialSol["colNum"]:
            initialSol["list"] = x
            initialSol["colNum"] = z
        itr += 1
    print("/-----------------------Resultados de Temperatura-----------------------/")
    print(f"La menor solucion encontrada tiene {initialSol['colNum']} colisiones")
    print(f"Tablero:")
    print(tabulate(createTable(initialSol["list"]), tablefmt="fancy_grid"))
    return initialSol
