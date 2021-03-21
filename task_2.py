"""Закодируйте любую строку по алгоритму Хаффмана"""

from collections import Counter


class MyNode:
    def __init__(self, value=None, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def __repr__(self):
        return f'{self.value}=>{self.left} - {self.right}'


def tree(data):  # Создание дерева по строке
    cnt = Counter()
    for key, value in Counter(data).items():
        cnt[MyNode(key)] = value
    spam = cnt.most_common()  # отсортированный список узлов
    eggs = None
    while len(spam) > 1:
        eggs = MyNode()
        eggs.left = spam[-2][0]
        eggs.right = spam[-1][0]
        count = spam[-1][1] + spam[-2][1]
        del spam[-2:]
        spam.append((eggs, count))
        spam.sort(key=lambda item: item[1], reverse=True)
    return eggs


def get_path(tree_, tmp_dict, path=''):  # рекурсивный обход дерева
    if tree_.value is not None:
        tmp_dict[tree_.value] = path
    else:
        get_path(tree_.left, tmp_dict, f'{path}0')
        get_path(tree_.right, tmp_dict, f'{path}1')
    return tmp_dict


def haff_table(data):  # создание таблицы кодирования
    haff_tree = tree(data)  # Создание дерева
    return get_path(haff_tree, {})


def code_text(data):  # кодирование строки
    spam = haff_table(data)
    res = ''
    for letter in data:
        res += spam[letter]
    return res


my_string = 'мама мыла раму'
print(haff_table(my_string))
print(code_text(my_string))
