import time
def time_on_function(funk):
    def wrapped(*args):
        start = time.time()
        result = funk(*args)
        print(time.time() - start)
        print(*args)
        return result
    return wrapped

@time_on_function
def funk(one, two):
    return one + two
print(f'А результат у нас {funk(1, 2)}')