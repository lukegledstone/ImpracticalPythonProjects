import load_dictionary
from main import load
word_list = load_dictionary.load('2of4brif.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)
print(*pali_list)