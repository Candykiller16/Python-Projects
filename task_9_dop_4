def decorator(funk):
    def wrapper(*args):
        return funk(*args)[::-1]
    return wrapper

@decorator
def start(l1,l2):
    return [l1,l2]

print(start([1,2], [3,4]))
