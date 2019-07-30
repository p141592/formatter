import os

from parser.parser import Parser

SOURCE_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ), 'source')


if __name__ == '__main__':
    documents = Parser().read_all_source(SOURCE_DIR)
    print(documents)

