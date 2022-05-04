def BruteForcecutrod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1,n+1):
        q = max(q, p[i] + BruteForcecutrod(p, n - i))
    return q
def MemorizedCutRod(p, n):
    R = [-1] * (n + 1) # inicialización de matriz
    def MemorizedCutRodAux(p, n, R):
        if R[n] >= 0:
            return R[n]
        q = -1
        if n == 0:
            q = 0
        else:
            for i in range(1, n + 1):
                q = max(q, p[i] + MemorizedCutRodAux(p, n - i, R))
        R[n] = q
        return q
    return MemorizedCutRodAux(p, n, R)#,R
def BottomUpCutRod(p, n):
    r = [0]*(n+1)
    for i in range(1, n+1):
        if n == 0:
            return 0
        q =0
        for j in range(1, i+1):
            q = max(q, p[j]+r[i-j])
            r[i] = q
    return r[n]#,r
