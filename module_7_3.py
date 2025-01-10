from os import remove
from pprint import pprint
import string
class WordsFinder:

    all_words = {}
    find_word = {}
    cou = {}


    def __init__(self, *names):
        self.names = list(names)

    def get_all_words(self):
        for i in self.names:
            with (open(i, encoding='utf-8') as file):
                words = file.read().lower()
                for j in string.punctuation:
                    if j in words:
                        words = words.replace(j, '')
                words = words.split()
                self.all_words[i] = words

    def find(self, word):

        for name, i in self.all_words.items():
            if word in i:
                self.find_word[name] = i.index(word)+1
        print(self.find_word)

    def count(self, word):

        for name, n in self.all_words.items():
            self.cou[name] = n.count(word)
        print(self.cou)










w1 = WordsFinder('test.txt', 'products.txt')
print(w1.names)
w1.get_all_words()
print(w1.all_words)
w1.find('text')
w1.count('text')
