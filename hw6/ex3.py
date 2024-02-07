'''Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, в которой
ни один ферзь не бьет другого. Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали,
горизонтали или диагонали.
Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.'''

import random


# board_list = []
# while len(board_list) < 1:
#     board = []
#     while len(board) < 8:
#         x = random.randint(0, 7)
#         y = random.randint(0, 7)
#         if all(x != el[0] and y != el[1] and abs(x - el[0]) != abs(y - el[1]) for el in board):
#             board.append((x, y))
#     board_list.append(board)


'''board = [[0 for i in range(8)] for j in range(8)]


def setQueen(i, j):
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] += 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] += 1
    board[i][j] = -1

def removeQueen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] -= 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] -= 1
    board[i][j] = 0

def printPosition():
    abc = '12345678'
    ans = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append(abc[j] + str(i+1))
    print(', '.join(ans))

def solve(i):
    for j in range(8):
        if board[i][j] == 0:
            setQueen(i,j)
            if i == 7:
                printPosition()
            else:
                solve(i+1)
            removeQueen(i,j)

solve(0)'''


'''def conflict(state, col):
    # Конфликтная функция, строка - строка, столбец - столбец
    row = len(state)
    for i in range(row):
        if abs(state[i] - col) in (0, row - i):
            return True
        else:
            return False


def queens(num=8, state=()):
    # Функция-генератор
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def queenprint(solution):
    # Функция печати
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


for solution in list(queens(8)):
    print(solution)

print('  total number is ' + str(len(list(queens()))))
print('  one of the range is:\n')

queenprint(random.choice(list(queens())))'''


'''
from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True'''

'''board_list = []
def place_queens():
    for _ in range(4):
        board = [[0] * 8 for _ in range(8)]
        queens = []
        for row in range(8):
            column = random.randint(0, 7)
            while column in queens or not is_valid_queen(board, row, column):
                column = random.randint(0, 7)
            queens.append(column)
            board[row][column] = 1
        board_list.append(queens)

def is_valid_queen(board, row, column):
    for i in range(row):
        if board[i][column] == 1:
            return False
        if column - (row - i) >= 0 and board[i][column - (row - i)] == 1:
            return False
        if column + (row - i) < 8 and board[i][column + (row - i)] == 1:
            return False
    return True

print(place_queens())'''

'''board = [[0 for i in range(8)] for j in range(8)]


def setQueen(i, j):
    for x in range(8):
        board[x][j] += 1
        board[i][x] += 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] += 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] += 1
    board[i][j] = -1

def removeQueen(i, j):
    for x in range(8):
        board[x][j] -= 1
        board[i][x] -= 1
        if 0 <= i + j - x < 8:
            board[i + j - x][x] -= 1
        if 0 <= i - j + x < 8:
            board[i - j + x][x] -= 1
    board[i][j] = 0

def printPosition():
    # global data
    abc = '12345678'
    ans = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                ans.append((abc[j],i+1))
    # print(', '.join(ans))
    return ans

def solve(i):
    global data
    for j in range(8):
        if board[i][j] == 0:
            setQueen(i,j)
            if i == 7:
                # printPosition()
                data = data.append(printPosition())
                # print(printPosition())
            else:
                solve(i+1)
            removeQueen(i,j)

data = []
solve(0)

print(data)'''

from itertools import combinations

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

print(generate_boards())