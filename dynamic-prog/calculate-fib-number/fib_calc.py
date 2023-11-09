dic = {}

def fib(n):
    if n in dic:
        return dic[n]
    
    if n<=2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    dic[n] = result
    return result

print(fib(4))
print(fib(50))