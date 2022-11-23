from graph import Graph

# Class for storing information regarding each vertex
class Vertex:
    def __init__(self, value: int, previous: int, locked: bool, distance: int):
        self.value = value
        self.previous = previous
        self.locked = locked
        self.distance = distance # total distance from start vertex

def dijkstragraph(original_graph: Graph, start: int):
    
    # Creating a copy of the original graph matrix
    graph = Graph(original_graph.matrix.copy())

    # Defining the verteces
    verteces = [None] * graph.size
    for i in range(0, graph.size):
        verteces[i] = Vertex(i, None, False, 10000)
    verteces[start] = Vertex(start, start, True, 0)

    # Storing the neighbours of each vertex from the graph matrix
    neighbours = [[None]] * graph.size
    for i in range(0, graph.size):
        neighbours[i] = []
        for j in range(0, graph.size):
            if graph.matrix[i][j] != 0:
                neighbours[i].append([j, graph.matrix[i][j]])

    # Recursive call
    verteces = dijkstra_help(neighbours, start, verteces)
    
    # Building the matrix
    for i in range(0, graph.size):
        graph.matrix[i] = [0] * graph.size
        for j in range(0, graph.size):
            if verteces[j].previous == i:
                graph.matrix[i][j] = verteces[j].distance - verteces[i].distance # weight of a single edge

    # Clearing lists
    verteces.clear()
    neighbours.clear()

    return graph

def dijkstra_help(neighbours: list, current: int, verteces: list):
    # Finding the current min distance among the verteces
    min_distance = 1000
    min_index = None

    # Finding the current minimum distance among verdices
    for vertex in verteces:
        if not vertex.locked and vertex.distance < min_distance:
            min_distance = vertex.distance
            min_index = vertex.value

    # Updating the distances for neighbours and finding the minimum distance
    for neighbour in neighbours[current]: # processing the neighbours of the current vertex
        i = neighbour[0]
        distance = neighbour[1]
        if not verteces[i].locked: # only process if neighbour is not locked
            new_distance = verteces[current].distance + distance
            if new_distance < verteces[i].distance:
                verteces[i] = Vertex(i, current, False, new_distance)
            if new_distance < min_distance:
                min_distance = new_distance
                min_index = i

    if min_index != None: # if there is verteces to process
        verteces[min_index].locked = True
        verteces = dijkstra_help(neighbours, min_index, verteces) # next recursion

    return verteces


if __name__ == "__main__":

    matrix = [
        [0, 25,  6,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, 10,  3,  0,  0,  0,  0,  0],
        [0,  0,  0,  7,  0, 25,  0,  0,  0,  0],
        [0,  0,  0,  0, 12, 15,  4, 15, 20,  0],
        [0,  0,  0,  0,  0,  0,  0,  2,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,  2,  0],
        [0,  0,  0,  0,  0,  0,  0,  8, 13, 15],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  5],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  1],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        ]

    m = [
        [0, 11, 6, 10, 0],
        [11, 0, 3, 6, 4],
        [6, 3, 0, 2, 0],
        [10, 6, 2, 0, 6],
        [0, 4, 0, 6, 0]
    ]

    graph = Graph(m)


    new_graph = dijkstragraph(graph, 0)
    
    print(new_graph.matrix)
    new_graph.df_print(0)           # 0 1 2 3 4 5 6 7 9 8 
    new_graph.bf_print(0)           # 0 1 2 3 4 5 6 7 8 9
    