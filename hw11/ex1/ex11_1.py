'''Создайте класс MyStr, который наследуется от встроенного класса str и добавлять дополнительную информацию
о создателе строки и времени ее создания. Этот класс будет представлять строки с информацией о событиях.
Класс MyStr должен иметь следующие атрибуты и методы:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'.

Магические методы (Dunder-методы):
Реализуйте метод __new__(cls, value, author), который создает новый объект класса MyStr с заданным value и author.
Метод также автоматически фиксирует время создания записи. В этом методе создается новый объект MyStr с указанными атрибутами
и текущим временем в атрибуте time.

Реализуйте метод __str__(self), который возвращает строковое представление объекта класса MyStr с информацией о событии,
авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление объекта класса MyStr.
Метод __repr__ возвращает строку, которая может быть использована для создания точно такого же объектаMyStrс теми же значениями value и author'''

from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author_name):
        my_srt = super().__new__(cls, value)
        my_srt.value = value
        my_srt.author_name = author_name
        my_srt.creation_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return my_srt

    def __str__(self):
        return f'{self.value} Автор: {self.author_name},Время создания: {self.creation_time }'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author_name}')"

# event = MyStr("Завершилось тестирование", "John")
# print(event)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))