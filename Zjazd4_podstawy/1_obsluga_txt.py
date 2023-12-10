
from functions import *

with open ('u2.txt', 'r', encoding='utf8') as file1:
    content = file1.read()

print(f'Liczba slow {no_of_words(content)}')
print(f'Liczba roznych slow {no_of_unique_words(content)}')

words_repeat(content)

print(my_dict)