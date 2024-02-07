# a = float(input("Сторона a = "))
# b = float(input("Сторона b = "))
# c = float(input("Сторона c = "))
#
# if a + b > c and a + c > b and b + c > a:
#     print("Треугольник существует")
#     if a == b and a == c and b == c:
#         print("Треугольник равносторонний")
#     elif a == b or a == c or b == c:
#         print("Треугольник равнобедренный")
#     else:
#         print("Треугольник разносторонний")
# else:
#     print("Треугольник не существует")


# num = int(input("Введите число для проверки : "))
#
# def check_simple(num):
#     for i in range(2, int(num ** (1 / 2) + 1)):
#         if num % i == 0:
#             return False
#     return True
#
# if num <= 1 or num > 100000:
#     print("Число должно быть больше 1 и меньше 100000")
# else:
#     if check_simple(num) == True:
#         print(f'Число {num} просоте')
#     else:
#         print(f'Число {num} составное')


'''
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

print(f'Количество совпадающих чисел: {len(set(list1).intersection(list2))}')'''

# coincidences = len(set(list1).intersection(list2))
# print(sorted(list1))
# print(sorted(list2))
# print(set(list1).intersection(list2))

'''from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

print(check_queens(queens = [(8,1), (3,2), (1,3), (6,4), (2,5), (5,6), (7,7), (4,8)] ))
print(check_queens(queens = [(8,1)] ))
print(check_queens(queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] ))
print(check_queens(queens = [] ))
print(check_queens(queens = [(8,1), (3,2), (1,3), (6,4), (2,5), (5,6), (7,7), (4,8)] ))'''

'''import random
from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True


def queens_rnd():
    queens = []
    for _ in range(1, 9):
        queens.append([random.randint(1, 8), random.randint(1, 8)])
    return queens

def generate_positions():
    positions = queens_rnd()
    for i in range(4):  # 4 успешные расстановки
        random.shuffle(positions)  # перемешиваем список
        while not check_queens(positions):  # если расстановка не успешная, перемешиваем ещё раз
            random.shuffle(positions)
        print(positions)  # выводим успешную расстановку

generate_positions()'''