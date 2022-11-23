def triangle(a, b, c):

    # if a side has negative length
    if a < 0 or b < 0 or c < 0:
        return False

    if b > a: # defining the longest side
        if c > b:
            x = c
            y = [a, b]
        else:
            x = b
            y = [a, c]
    else:
        x = a
        y = [b, c]

    # checking if its possible to form a tringle
    if x >= y[0] + y[1]:
        return False
    else:
        return True

if __name__ == "__main__":
    print(triangle(3, 5, 4))    # True
    print(triangle(-1, 2, 3))   # False
    print(triangle(5, 9, 14))   # False
    print(triangle(30, 12, 29)) # True