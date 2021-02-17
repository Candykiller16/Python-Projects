stroka = 'a', 't', 'd', 'r', 't', 'd', 'q', 'e'
zrez_stroki = int(len(stroka)/2)
print(stroka[zrez_stroki])
if stroka[zrez_stroki] == stroka[1]:
    print(stroka[1:])
else:
    print('Усё добра')
