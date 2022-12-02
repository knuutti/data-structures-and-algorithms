def salesman(city_map):
    n = len(city_map[0])
    edges = {}

    for i in range(0, n-1):
        for j in range(i+1, n):
            edges[f"{i};{j}"] = city_map[i][j]

    path = [0]
    rows = [0] * (2*n)
    edge_count = 0

    path_matrix = [[0] * n for i in range(0,n+1)]

    for edge in sorted(edges, key=edges.get):
        cities = edge.split(';')

        start = int(cities[0])
        end = int(cities[1])

        if rows[start] < 2 and rows[end+n] < 2: # makes sure that a node can only have two edges
            rows[start] += 1
            rows[end+n] += 1
            edge_count += 1

            path_matrix[start][end] = city_map[start][end]
            path_matrix[end][start] = city_map[start][end]

            if edge_count == n:
                break

    current = 0
    visited = []
    visited.append(1)
    for i in range(1, n):
        visited.append(0)

    for i in range (0, n):
        for j in range(0, n):
            if not path_matrix[current][j] or visited[j] == 1:
                continue
            else:
                current = j
                path.append(current)
                visited[current] = 1
                break
    path.append(path[0])

    print(path)
    print(f"Number of cities is {n}")
    print(path_matrix)

    return path
    

if __name__ == "__main__":
    
    cost = 0

    adj = [[0, 10, 15, 20],
       [10, 0, 35, 25],
       [15, 35, 0, 30],
       [20, 25, 30, 0]]

    city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

    path = salesman(adj)
    for i in range(len(adj)):
        cost += adj[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45