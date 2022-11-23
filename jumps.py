def jumps(n, a, b):
    # List for storing values
    list = [0] * (n+1)
    list[0] = 1 # base case

    # Solving the jumps at n'th position iteratively
    for i in range(1, n+1):
        list[i] = list[i-a] + list[i-b]

    return list[n]

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937