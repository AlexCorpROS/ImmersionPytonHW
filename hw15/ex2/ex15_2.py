'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним, только если треугольник существует.'''
import logging
import  argparse

FORMAT = ("{asctime} - {levelname}: {msg}")
logging.basicConfig(filename='log/ex15_2.log', filemode='a', format=FORMAT, encoding='utf-8', style='{', level=logging.INFO)
logger = logging.getLogger('main')

parser = argparse.ArgumentParser(description="argument parser")
parser.add_argument('-a', metavar=' side_triangle_a', type= int or float , default=1, help='Задайте сторону А')
parser.add_argument('-b', metavar=' side_triangle_b', type= int or float , default=1, help='Задайте сторону B')
parser.add_argument('-c', metavar=' side_triangle_c', type= int or float , default=1, help='Задайте сторону C')
args = parser.parse_args()

def triangle(a = 1, b = 1, c=1):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if a == b == c:
            print("Треугольник равносторонний")
            logger.info(f'Треугольник равносторонний. Стороны а = {a}, b = {b}, c = {c}')
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
            logger.info(f'Треугольник равнобедренный. Стороны а = {a}, b = {b}, c = {c}')
        else:
            print("Треугольник разносторонний")
            logger.info(f'Треугольник разносторонний. Стороны а = {a}, b = {b}, c = {c}')
    else:
        print("Треугольник не существует")
        logger.warning(f'Треугольник со сторонами а = {a}, b = {b}, c = {c} не существует.')


if __name__ == '__main__':
    triangle(float(args.a),float(args.b),float(args.c))

# if __name__ == '__main__':
#     triangle(2,1,1)
#     print('-----------')
#     triangle(222,2,2)

# pyton .\ex15_2.py -a 2 -b 2 -b 2