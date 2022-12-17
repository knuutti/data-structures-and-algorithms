
def recursion(n):
    if n == 1 or n == 0:
        return n
    else:
        return recursion(n - 1) + recursion(n - 2)

combs = recursion(7)
print(combs)
    
