def count(path, graph):
    sum = 0
    for i in range(len(path)-1):
        sum += graph[path[i]][path[i+1]]
    return sum