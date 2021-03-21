# Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.
#
# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.
#
# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

# a = str(input())
#
# index = 0
# count = 1
#
#
# for i in range(index, len(a) - 1):
#     if a[index] == a[index + 1]:
#         count += 1
#     else:
#         print(a[index] + str(count), end='')
#         count = 1
#     index +=1
# print(a[index] + str(count), end='')

# Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
#
# Если на вход пришло только одно число, надо вывести его же.
#
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# a = [int(i) for i in input().split()]
# b = []
# if len(a) == 1:
#     print(*a)
# else:
#     for i in range(len(a)-1):
#         b.append(a[i-1] + a[i+1])
#     b.append(a[0] + a[-2])
# print(*b)

# Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
#
# Для решения задачи может пригодиться метод sort списка.
#
# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.


# a, b = [int(i) for i in input().split()], []
# for i in a:
#     if a.count(i) > 1 and b.count(i) == 0:
#         b.append(i)
# for i in b:
#     print(i, end=" ")

# a =[int(i) for i in input().split()]
# a.sort()
# b = []
# for i in range(1, len(a)):
#     if a[i] == a[i-1]:
#         #print(a[i], end=' ')
#         if a[i] not in b:
#             b.append(a[i])
# for i in range(0, len(b)):
#     print(b[i], end =' ')


#
# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')
#
# str = [int(i) for i in input().split()]
# ans = []
# [ans.append(x) for x in str if x not in ans and str.count(x) > 1]
# print(*ans)