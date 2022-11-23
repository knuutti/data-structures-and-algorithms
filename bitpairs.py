def pairs(s):
    sumOfIndex = 0
    totalOnes = 0
    totalSum = 0

    for i in range(len(s)):
        if s[i] == "1":

            totalOnes = totalOnes + 1
            sumOfIndex = sumOfIndex + len(s)-i-1
            totalSum = totalSum + sumOfIndex - totalOnes * (len(s)-i-1)

    return totalSum


if __name__ == "__main__":
    print(pairs("100101")) # 10
    print(pairs("101")) # 2
    print(pairs("100100111001")) # 71