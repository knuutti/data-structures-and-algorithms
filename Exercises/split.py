def split(T):

    sum = 0

    listLtoR = T.copy()
    listRtoL = T.copy()

    splitsLtoR = [0] * len(T)

    splitsRtoL = [0] * len(T)
    
    # from left to right
    for i in range(len(T)-1):
        if listLtoR[i+1] < listLtoR[i]:
            listLtoR[i+1] = listLtoR[i]
            splitsLtoR[i+1] = 0
        elif listLtoR[i+1] > listLtoR[i]:
            splitsLtoR[i+1] = 1
        else:
            splitsLtoR[i+1] = 0
    
    # from right to left
    for j in range(len(T)-1):
        k = len(T)-j-1
        if listRtoL[k-1] > listRtoL[k]:
            listRtoL[k-1] = listRtoL[k]
            splitsRtoL[k] = 0
        elif listRtoL[k-1] < listRtoL[k]:
            splitsRtoL[k] = 1
        else:
            splitsRtoL[k] = 0

    for l in range(len(T)):
        if splitsRtoL[l] == 1 and splitsLtoR[l] == 1:
            sum = sum + 1

    return sum


if __name__ == "__main__":
    print(split([1,2,3,4,5])) # 4
    print(split([5,4,3,2,1])) # 0
    print(split([2,1,2,5,7,6,9])) # 3
    print(split([1,2,3,1])) # 0