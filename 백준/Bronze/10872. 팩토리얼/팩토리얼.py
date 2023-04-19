def factorial(x):
    # 1! = 1, 0! = 1
    if x == 1 or x == 0: return 1
    # x! = x * (x-1)!
    return x * factorial(x - 1)

n = int(input())
print(factorial(n))