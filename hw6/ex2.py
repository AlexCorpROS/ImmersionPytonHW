'''Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь. Не забудьте напечатать результат.'''

# def check_queens(**data):
#     data = data['queens']
#     n = len(data)
#     x = []
#     y = []
#     for el in data:
#         x.append(el[0])
#         y.append(el[1])
#     if n <= 1:
#         return True
#     else:
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#                     return False
#                 else:
#                     return True

'''def check_queens(**data):
    data = data['queens']
    n = len(data)
    x = []
    y = []
    result = []
    for el in data:
        x.append(el[0])
        y.append(el[1])
    print(x,y)
    if n <= 1:
        return True
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    return False
                else:
                    return True'''


def check_queens(**data):
    data = data['queens']
    n_lst = len(data)
    x = []
    y = []
    result = []
    for el in data:
        x.append(el[0])
        y.append(el[1])
    if n_lst <= 1:
        return True
    else:
        for i in range(n_lst):
            for j in range(i + 1, n_lst):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    result.append(1)
                else:
                    result.append(0)
    print(result)
    if any([el == 1 for el in result]):
        return False
    else:
        return True

'''print(check_queens(queens = [(5,1), (1,2)] ))
print(check_queens(queens = [(1,1)] ))
print(check_queens(queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]))

print(check_queens(queens = [(8,1), (3,2), (1,3), (6,4), (2,5), (5,6), (7,7), (4,8)] )) # True
'''
print(check_queens(queens = [(8,1), (4,2), (1,3), (3,4), (6,5), (2,6), (7,7), (5,8)] )) # True

print(check_queens(queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] ))



'''from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True'''

