def cut_rod1(p, n):
    if n == 0:
        return 0
    q = -10000
    for i in range(1,n+1):
        a = p[i] + cut_rod1(p,n-i)
        if q < a:
            q = a
    return q

def cut_rod2(p, n):
    r = [0] * (n+1)
    for j in range(1,n+1):
        q = -10000
        for i in range(1,j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
        r[j] = q
    return r[n]

price = range(31)
print(cut_rod1(price,30))
print(cut_rod2(price,30))