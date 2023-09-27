def power2nA(n):
    return 2**n

print(power2nA(3))

def power2nB(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return power2nB(n-1) + power2nB(n-1)

print(power2nB(3))
        
def power2nC(n):
    if n == 0:
        return 1
    return 2 * power2nC(n-1)

print(power2nC(4))

fib = [None] * 10000
fib[0] = 1
fib[1] = 2
def power2nD(n):
    if not fib[n] is None: 
        return fib[n]
    fib[n] = power2nD(n-1) + power2nD(n-1)
    return fib[n]

print(power2nD(4))
#此作業是經由111010529顏瑋成同學教導後自行理解所完成
