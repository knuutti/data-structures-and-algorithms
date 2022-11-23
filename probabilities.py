import random


def algorithm(L):
    k = 0
    for i in range(1,L+1):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1:
            k = k + 1
    return 4 * k / L

print(algorithm(40000))