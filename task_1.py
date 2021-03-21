"""Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке. """

import hashlib


def substrings(data):
    spam = {}
    len_ = len(data)
    for i in range(len_):
        for j in range(i, len_ + 1):
            eggs = hashlib.sha1(data[i:j].encode('utf-8')).hexdigest()
            if eggs not in spam:
                spam[eggs] = 1

    return len(spam) - 2


my_string = 'papa'
print(substrings(my_string))
