from graph import Graph

# Class for storing data on each vertex
class Vertex:
    def __init__(self, value):
        self.value = value
        self.root = value
        self.parent = value
        self.children = []
        self.edges = {}

# Function for sorting the edges (uses dictionary)
def edgeSort(verteces):

    # Storing each edge to a dictionary
    edge_dict = {}
    for v in verteces:
        for child in v.edges:
            edge_dict[f"{v.value},{child}"] = v.edges[child]

    # Sorting the dictionary based on edge weight
    edges = sorted(edge_dict, key=edge_dict.get)

    # Storing sorted edges to a list only once (e.g. 3-2 is not added if 2-3 exists)
    sorted_edges = []
    for edge in edges:
        values = edge.split(',')
        start = int(values[0].lstrip('\''))
        end = int(values[1].rstrip('\''))
        if [end,start] not in sorted_edges:
            sorted_edges.append([start,end])

    return sorted_edges

def kruskal(graph):

    # List of verteces
    verteces = []
    for i in range(0, graph.size):
        verteces.append(Vertex(i))
        for j,weight in enumerate(graph.matrix[i]):
            if weight:
                verteces[i].edges[j] = graph.matrix[i][j]

    # Sorting the edges based on weight
    sorted_edges = edgeSort(verteces)

    # Going through the edges (greedy algorithm)
    for edge in sorted_edges:
        start = edge[0]
        end = edge[1]

        # Edge already unioned -> skip
        if verteces[start].root == verteces[end].root: 
            continue

        # Connecting vertex with a parent vertex
        if verteces[end].root != end and verteces[start].root == start:
            verteces[start].parent = end
            verteces[end].children.append(start)
        
        # Connecting vertex with a child vertex -> must update parent
        else:
            verteces[verteces[end].parent].parent = end
            verteces[start].children.append(end)
            verteces[end].parent = start

        # Update root vertex for each vertex
        for v in verteces:
            v.root = verteces[v.parent].root

    # Building the matrix
    D = [None] * graph.size
    for i in range(0, graph.size):
        D[i] = [0] * graph.size
        
    for i,vertex in enumerate(verteces):
        for j in vertex.children:
            D[i][j] = graph.matrix[i][j]
            D[j][i] = graph.matrix[i][j]
        
    # Creating the new graph
    mst = Graph(D)

    return mst

if __name__ == "__main__":
    matrix = [
    #    0  1  2  3  4  5
        [0, 0, 7, 6, 9, 0], # 0
        [0, 0, 5, 0, 0, 6], # 1
        [7, 5, 0, 1, 0, 2], # 2
        [6, 0, 1, 0, 0, 2], # 3
        [9, 0, 0, 0, 0, 1], # 4
        [0, 6, 2, 2, 1, 0]  # 5    
    ]

    graph = Graph(matrix)
    graph.bf_print(0)   # 0 2 3 4 1 5
    mst = kruskal(graph)
    print(mst.matrix)
    mst.bf_print(0)     # 0 3 2 1 5 4