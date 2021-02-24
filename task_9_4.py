spisok = [19, 26, 39, 116, 38, 57, 256, 98, 30, 300, 500, 1919, 600]
result = filter(lambda x: x%19 ==0 or x%30 ==0, spisok)
print(list(result))