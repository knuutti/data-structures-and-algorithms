def primes(N):
    x = 0 # the amount of primes

    for i in range(N+1):
        if i > 1:
            notPrime = False # variable for breaking the loop when number is proven prime
            for j in range(2, i):
                notPrime = False
                if (i % j) == 0:
                    notPrime = True
                    break
            if notPrime == False:
                x = x + 1

    return x

if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15