'''Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
На вход будет подаваться дата в формате "день.месяц.год".
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.'''

date_to_prove = '15.4.9955'


def func(date):
    day, month, year = map(int, date.split('.'))
    if year in range(0, 10000) and month in range(1, 13) and day in range(1, 32):
        if month == 2:
            if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                if day in range(1, 30):
                    return True
                else:
                    return False
            elif day in range(1, 29):
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return True
        else:
            if day in range(1, 31):
                return True
            else:
                return False
    else:
        return False

print(func(date_to_prove))