from numpy import arange
import math

def f(x) :
    # return x*x-4*x+1
    return x*x - 3*x + 1

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        print("x=", x, " f(x)=", f(x)) 

#此作業是經由111010529顏瑋成同學教導後自行理解所完成
