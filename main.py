import os

from parser import Parser

SOURCE_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ), 'source')

_articles = []


def read_all_source():
    for root, dirs, files in os.walk(SOURCE_DIR):
        for _file in files:
            file = os.path.join(root, _file)
            _articles.append(Parser(file).start())


if __name__ == '__main__':
    print('='*50)
    print(SOURCE_DIR)
    read_all_source()
    print(_articles)
