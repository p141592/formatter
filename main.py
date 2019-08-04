import datetime
import os

from parser.parser import Parser

SOURCE_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ), 'source')


if __name__ == '__main__':
    START_TIME = datetime.datetime.now()
    tree_root = Parser().read_all_source(SOURCE_DIR)
    print(f'RESULT TREE: {tree_root}')
    # print(f'TRANSLATE PRICE: \n'
    #       f'{Translate(tree_root).get_price()}')
    FINISH_TIME = datetime.datetime.now()
    DURATION = FINISH_TIME - START_TIME
    print(f'= DURATION: {DURATION}')
