def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    num1 = 0
    num2 = 1
    sum1 = 0
    
    for i in range(2, n+1, 1):
        sum1 = num1 + num2
        num1 = num2
        num2 = sum1
    return sum1
      
print(fib(5))
