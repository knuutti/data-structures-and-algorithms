def permutations(n, k, numbers, included, list):
    if k == n:
        list.append(numbers.copy())
    else:
        for i in range(0,n):
            if not included[i]:
                included[i] = True
                numbers[k] = i+1
                list = permutations(n, k+1, numbers, included, list)
                included[i] = False
    
    return list

if __name__ == "__main__":
    n = 5
    list = []
    included = [None] * n
    numbers = [None] * n
    list = permutations(n,0, numbers, included, list)
    print(list[99])