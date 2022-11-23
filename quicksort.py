def partition(A, low, high):
 
    # Lets select the middle of the list as the pivot value and swap it with the last value
    pivotindex = high
    pivot = A[pivotindex]
    print(pivot)
    (A[pivotindex], A[high]) = (A[high], A[pivotindex])
 
    i = low - 1 # pointer for seeking greater element 
 
    # Lets loop through all the values in the list, comparing to the pivot value
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            # If the value is less than the pivot value, swap it with the value at position i (which is greater value)
            (A[i], A[j]) = (A[j], A[i])
 
    # As the last step, swap the pivot value with the value at position i+1
    (A[i + 1], A[high]) = (A[high], A[i + 1])
 
    return i + 1
 
def qsort(A, i, j):
    if i < j:
        k = partition(A, i, j)
        # Sorting the left side of the pivot
        qsort(A, i, k - 1)
        # Sorting the right side of the pivot
        qsort(A, k + 1, j)
    
    return
    


if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    print(A)    # [9, 7, 1, 8, 5, 3, 6, 2, 4]
    qsort(A, 0, len(A)-1)
    print(A)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]