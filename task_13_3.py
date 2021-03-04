f = open('text123.txt')
def gen():
    for line in f:
        yield line
g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))