class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(self.matrix[0])

    # Prints the graph in depth-first-order
    def df_print(self, start) -> list:
        visited = [start]
        visited = self.df_help(start, visited)
        for node in visited:
            print(node, end=" ")
        print()
        return 

    # Help function for DFO recursion
    def df_help(self, start, visited) -> list:
        for i in range(0, self.size):
            if i == start or self.matrix[start][i] == 0 or i in visited:
                continue
            visited.append(i)
            visited = self.df_help(i, visited)
        return visited

    # Prints the graph in breadth-first-order
    def bf_print(self, start) -> list:
        visited = [start]
        queue = [start]
        visited = self.bf_help(start, visited, queue)
        for node in visited:
            print(node, end=" ")
        print()
        return

    # Help function for BFO recursion
    def bf_help(self, start: int, visited: list, queue: list) -> list:
        queue.remove(start) # removing the visited node from queue
        for i in range(0, self.size):
            if i == start or self.matrix[start][i] == 0:
                continue
            elif i not in visited:
                visited.append(i)
                queue.append(i)
        for i in queue:
            visited = self.bf_help(i, visited, queue)
        return visited

    # Calculates the edge weight, returns -1 if none
    def weight(self, start, end) -> int:
        weight = self.matrix[start][end]
        if weight == 0:
            weight = -1
        return weight
    


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

    graph.df_print(0)           # 0 2 1 3 5 4 
    graph.bf_print(0)           # 0 2 4 1 3 5 
    print(graph.weight(0, 2))   # 7
    print(graph.weight(3, 4))   # -1