import re
from collections import Counter

def ten_most_freq(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = 'Hello world. Hello Python. Hello again.'
print(ten_most_freq(text))