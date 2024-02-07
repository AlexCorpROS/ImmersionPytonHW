'''Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''

# num = int(input('Введите целое число: '))
#
# def convers_hex(number: int) -> str:
#     if not number:
#         return '0x0'
#     result = ''
#     let_hex = list('0123456789abcdef')
#     while number > 0:
#         result = let_hex[number % 16] + result
#         number //= 16
#     return result
# print(f'Число {num} в шестнадцатиричном виде  -> {convers_hex(num)}')
# print(f'Проверка результата: {hex(num)}')


# num = 255
# def convers_hex(number: int) -> str:
#     result = ''
#     let_hex = list('0123456789abcdef')
#     while number > 0:
#         result = let_hex[number % 16] + result
#         number //= 16
#     return result
# print(f'Шестнадцатеричное представление числа: {convers_hex(num).upper()}')
# print(f'Проверка результата: {hex(num)}')

'''На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
Напишите программу, которая должна возвращать сумму и произведение дробей.
Для проверки своего кода используйте модуль fractions.'''

from fractions import Fraction

frac1 = '1/2'
frac2 = '1/3'

num1, denom1 = map(int, frac1.split("/"))
num2, denom2 = map(int, frac2.split("/"))

sum_frac_num = num1 * denom2 + num2 * denom1
sum_frac_denom = denom1 * denom2
prod_frac_num = num1 * num2
prod_frac_denom = denom1 * denom2

f1 = Fraction(num1,denom1)
f2 = Fraction(num2,denom2)

print(f'Сумма дробей: {sum_frac_num}/{sum_frac_denom}')
print(f'Произведение дробей: {prod_frac_num}/{prod_frac_denom}')
print(f'Сумма дробей: {f1+f2}')
print(f'Произведение дробей: {f1*f2}')

