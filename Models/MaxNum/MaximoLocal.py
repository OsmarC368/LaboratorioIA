import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as geek

def solve(function, rang, iter):
    min = [0, 99999999999999999999999999]
    listIter = []
    n = (rang[1] - rang[0]) / iter
    print(f"El valor del desplazamiento es {n}")
    for i in range(iter):
        z = rang[0] + (n*i)
        print(f"X: {z} Y: {function(z)}")
        listIter.append({"X":z, "Y":function(z)})
        if function(z) < min[1]:
            min[0] = z
            min[1] = function(z)
    
    print(f"\nEL Minimo Y es: {min[1]}\nDado por el Valor X: {min[0]}")
    return min, listIter


def graph(rang, min, funcion):
    x = geek.linspace(float(rang[0]), float(rang[1]), num=600)
    # x = geek.arange(rang[0], rang[1], 0.01)
    y = [funcion(z) for z in x]
    plt.plot(x, y)
    plt.grid(True)
    plt.axvline(min[0], color="red", linestyle="--")
    plt.title("Grafico de la Funcion", loc="center", fontsize=16)
    plt.legend(["Funcion", "Minimo"])
    plt.rc('axes', axisbelow=True)
    plt.xlabel("Cantidad")
    plt.ylabel("Costo")
    plt.show()

# result = solve(lambda x: (x**4) - (4*(x**3)) + (7*x), [-2,4], 100)

# graph([-2,4], result, lambda x: (x**4) - (4*(x**3)) + (7*x))