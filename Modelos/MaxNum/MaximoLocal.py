def solve(function, rang, iter):
    min = [0, 99999999999999999999999999]
    n = (rang[1] - rang[0]) / iter
    print(f"El valor del desplazamiento es {n}")
    for i in range(iter):
        z = rang[0] + (n*i)
        print(f"X: {z} Y: {function(z)}")
        if function(z) < min[1]:
            min[0] = z
            min[1] = function(z)
    
    print(f"\nEL Minimo Y es: {min[1]}\nDado por el Valor X: {min[0]}")

solve(lambda x: (x**3) - (2*x) + 3, [-1,5], 10)