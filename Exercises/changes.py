def changes(A):
    x = 0
    i = 0
    while i < len(A)-1:
        if A[i] == A[i+1]:
            if i < len(A)-2 and A[i+1] == A[i+2]:
                i = i + 1
            x = x + 1
        i = i + 1
    return x

if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2  