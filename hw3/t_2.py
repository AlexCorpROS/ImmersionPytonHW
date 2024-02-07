import re

text = "Installing Python is generally easy, and nowadays many Linux and UNIX distributions include a recent Python. Even some Windows computers (notably those from HP) now come with Python already installed. If you do need to install Python and arent confident about the task you can find a few notes on the BeginnersGuide/Download wiki page, but installation is unremarkable on most platforms."

# Удаляем знаки препинания и цифры
text_modified = re.sub("[^A-Za-z]", " ", text)

# Разбиваем текст на слова и считаем их количество
_dict = {}
for el in text_modified.lower().split():
    _dict[el] = _dict.get(el, 0) + 1

# Сортируем словарь посредством формирования списка (ключ, значение)
_list = []
for key, value in _dict.items():
    _list.append((key, value))
    _list.sort(key=lambda x: x[1], reverse=True)

# Печатаем первые 10 самых используемых слов
print(_list[0:10])


# import re
# from collections import Counter
#
# # Удаляем знаки препинания и приводим текст к нижнему регистру
# cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)
#
# # Разбиваем текст на слова и считаем их количество
# words = cleaned_text.split()
# word_counts = {}
#
# for word in words:
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1
#
# # Получаем 10 самых часто встречающихся слов
# top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
#
# print(top_words)