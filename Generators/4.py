def fun(a, b):
    for i in range(a, b + 1):
        yield i * i
a = int(input())
b = int(input())
for x in fun(a, b):
    print(x)