# Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или число более ста тысяч,
# выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
#
# Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.

def main():
    pass

if __name__ == '__main__':
    main()

# import logging
# import  argparse
#
# FORMAT = ("{asctime} - {levelname}: {msg}")
# logging.basicConfig(filename='log/ex15_3.log', filemode='a', format=FORMAT, encoding='utf-8', style='{', level=logging.INFO)
# logger = logging.getLogger('main')
#
# parser = argparse.ArgumentParser(description="argument parser")
# parser.add_argument('-num', metavar='number', type= int , default = 2, help='Введите целое число на проверку')
# args = parser.parse_args()
#
# def check_simple(num):
#     for i in range(2, int(num ** (1 / 2) + 1)):
#         if num % i == 0:
#             return False
#     return True
#
# def input_test(num):
#     if num < 2 or num > 100000:
#         print("Число должно быть больше 1 и меньше 100000")
#         logger.warning(f"Число должно быть больше 1 и меньше 100000. Вы ввели {num}")
#     else:
#         if check_simple(num) == True:
#             print(f'{num} является простым числом')
#             logger.info(f'Число {num} простое')
#         else:
#             print(f'{num} является составным числом')
#             logger.info(f'Число {num} составное')
#
# if __name__ == '__main__':
#     input_test(args.num)

# pyton .\ex15_3.py -num 17