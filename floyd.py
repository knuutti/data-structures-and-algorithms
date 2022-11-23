from graph import Graph

MAX = 10000

def floyd(graph):
    
    D = graph.matrix # original graph structure
    
    # Converting non-existing edges to edges with value MAX
    for i in range(0, graph.size):
        for j in range(0, graph.size):
            if D[i][j] == 0 and i != j: # only 0 values are on the diagonal
                D[i][j] = MAX

    for k in range(0, graph.size):
        for i in range(0, graph.size):
            for j in range(0, graph.size):
                # if there is a better path from vertex <i> to vertex <j> VIA vertex <k>,
                # change the path weight to that
                if D[i][k] != MAX and D[k][j] != MAX and D[i][j] > (D[i][k] + D[k][j]):
                    D[i][j] = D[i][k] + D[k][j]
    
    # Converting the MAX values back to 0
    for i in range(0, graph.size):
        for j in range(0, graph.size):
            if D[i][j] == MAX:
                D[i][j] = 0

    return D


if __name__ == "__main__":

    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 0, 9, 0], # 0
        [0, 0, 0, 0, 0, 0], # 1
        [0, 5, 0, 1, 0, 2], # 2
        [6, 0, 0, 0, 0, 2], # 3
        [0, 0, 0, 0, 0, 1], # 4
        [0, 6, 0, 0, 0, 0]  # 5   
    ]
    graph = Graph(matrix)
    D = floyd(graph)
    for i in range(6):
        for j in range(6):
            print(f"{D[i][j]:2d}", end=" ")
        print()
    #  0 12  7  8  9  9 
    #  0  0  0  0  0  0 
    #  7  5  0  1 16  2 
    #  6  8 13  0 15  2 
    #  0  7  0  0  0  1 
    #  0  6  0  0  0  0 