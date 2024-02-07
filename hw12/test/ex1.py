from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author_name):
        my_srt = super().__new__(cls, value)
        my_srt.value = value
        my_srt.author_name = author_name
        my_srt.creation_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return my_srt

    def __str__(self):
        return f'{self.value} (Автор: {self.author_name}, Время создания: {self.creation_time })'

    def __repr__(self):
        return f"MyStr('{self.value}', '{self.author_name}')"

event = MyStr("Завершилось тестирование", "John")
print(event)