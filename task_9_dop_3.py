
def decorator(funk):
    def wrapper(result):
        result = list(filter(lambda x: x%2 !=0, result))
        return result
    return wrapper

@decorator
def govno(result):
    return result

spisok_1 = [19, 26, 39, 116, 38, 57, 256, 98, 30, 300, 500, 1919, 600]
print(govno(spisok_1))
# или
print(govno([19, 26, 39, 116, 38, 57, 256, 98, 30, 300, 500, 1919, 600]))