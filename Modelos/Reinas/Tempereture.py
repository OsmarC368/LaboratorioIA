import random
from QueenModel import *
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


def solve():
    initialSol = {
        "list": [4,2,1,3,5,6,7,8,9],
        "colNum": countColisions(createTable([4,2,1,3]), [4,2,1,3]) 
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


solve()