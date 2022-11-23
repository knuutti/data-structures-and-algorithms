def search(A: list, item: int):
    a = 0
    b = len(A)-1
    while a <= b:
        k = (a+b)//2
        if A[k] == item:
            return k
        if A[k] < item:
            a = k+1
        if A[k] > item:
            b = k - 1
    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 6, 10, 15, 22, 27, 30, 31]
    print(search(A, 6))     # 3
    print(search(A, 7))     # -1
    print(search(A, 30))    # 8