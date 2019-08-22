import datetime
import os

from parser.db import DB
from parser.parser import Parser
from parser.source import GitSource
from parser.tree import BaseTree
from parser.tree.raw_nodes import Root

SOURCE_DIR = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ), 'source')


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


def read_all_source(dir):
    ALL_FILES = []
    ROOT = Root()

    for root, dirs, files in os.walk(dir):
        for _file in files:
            ALL_FILES.append(os.path.join(root, _file))

    FILES_LENGTH = len(ALL_FILES)

    print(f'DOCUMENTS IN QUEUE: {FILES_LENGTH}')

    items = list(ALL_FILES)
    l = len(items)

    printProgressBar(0, FILES_LENGTH, prefix='Progress:', suffix='Complete', length=50)
    for i, item in enumerate(items[:10]):
        _document = Parser(ALL_FILES.pop(), position=i).read_document()
        ROOT._append(_document)

        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)

    return ROOT

if __name__ == '__main__':
    START_TIME = datetime.datetime.now()
    print(START_TIME)

    with GitSource() as document:
        Parser(document).read()

        tree_root = read_all_source(SOURCE_DIR)

    print(f"Количество элементов в дереве: {len(tree_root)}")
    print("Запись в базу")

    tree_root.db_insert()

    print("Извлечение объекта из базы")
    tree2 = Parser.load_object(tree_root.id, db=DB())

    print(f'= DURATION: {datetime.datetime.now() - START_TIME}')
