def gen(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            yield line
a = gen('text123.txt')
print(next(a))
print(next(a))
print(next(a))
print(next(a))



