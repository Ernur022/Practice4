def fun(n):
    for i in range(n + 1):
        yield i * i
n = int(input())
for x in fun(n):
    print(x)