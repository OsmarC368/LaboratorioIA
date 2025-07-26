import matplotlib.pyplot as plt
import numpy as np

def createTable(qList):
    table = []
    for _ in range(len(qList)):
        aux = ["" for _ in range(len(qList))]
        table.append(aux)

    for i, x in enumerate(qList):
        table[x-1][i] = "Q"
    
    return table

def countColisions(table, qList):
    colisiones = 0
    for i, x in enumerate(qList):
        #check in X
        # colisiones += 1 if table[x-1].count("Q") >= 2 else 0

        #LEFT
        for z in range(len(qList)):
            if i-1-z >= 0:
                if table[x-1][i-z-1] == 'Q':
                    colisiones += 1
                    break
            else:
                break

        #RIGHT
        for z in range(len(qList)):
            if z+1+i < len(qList):
                if table[x-1][i+1+z] == "Q":
                    colisiones += 1
                    break
            else:
                break

        
        #No need to check Y since it will never be 2 queens in the same column
        #colisiones += [] se podria hacer de esta forma con un for if interno
        # pero de momento no parece ser neceseraio
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        #X Axis Up
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        for z in range(len(qList)):
            aux = colisiones
            upX = [(x-2)-z, i-z-1]
            #Count X
            if upX[0] >= 0 and upX[1] >= 0 and upX[0] < (len(qList)) and upX[1] < (len(qList)):
                colisiones += 1 if table[upX[0]][upX[1]] == "Q" else 0
            if aux != colisiones:
                break

        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        #X Axis Down
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        for z in range(len(qList)):
            aux = colisiones
            downX = [x+z, i+1+z]
            if downX[0] >= 0 and downX[1] >= 0 and downX[0] < (len(qList)) and downX[1] < (len(qList)):
                colisiones += 1 if table[downX[0]][downX[1]] == "Q" else 0    
            if aux != colisiones:
                break
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        #Y Axis Up
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        for z in range(len(qList)):
            aux = colisiones
            upY = [x-2-z, i+1+z]
            #Count Y
            if upY[0] >= 0 and upY[1] >= 0 and upY[0] < len(qList) and upY[1] < len(qList):
                colisiones += 1 if table[upY[0]][upY[1]] == "Q" else 0

            if aux != colisiones:
                break

        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        #Y Axis Down
        #-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/
        for z in range(len(qList)):
            aux = colisiones
            downY = [x+z, i-1-z]
            if downY[0] >= 0 and downY[1] >= 0 and downY[0] < (len(qList)) and downY[1] < (len(qList)):
                colisiones += 1 if table[downY[0]][downY[1]] == "Q" else 0    
            if aux != colisiones:
                break

    return colisiones


def graph(sol, colisions):
    tablero = np.zeros((len(sol),len(sol)))
    tablero[1::2, ::2] = 1
    tablero[::2, 1::2] = 1
    plt.imshow(tablero, cmap='gray', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])

    qPositions = []
    for i,x in enumerate(sol):
        qPositions.append((i, x-1))

    # Dibujar líneas de cuadrícula
    for i in range(len(sol)):
        plt.axhline(i - 0.5, color='black', linewidth=1)
        plt.axvline(i - 0.5, color='black', linewidth=1)

    for fila, col in qPositions:
        if colisions == 0:
            plt.text(col, fila, '♛', fontsize=30, ha='center', va='center', color='green')
        else:
            plt.text(col, fila, '♛', fontsize=30, ha='center', va='center', color='red')


    plt.title(f"♛ Tablero de Ajedrez {len(sol)}x{len(sol)}")
    plt.show()


