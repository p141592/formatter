# Разбор pandoc JSON
from formatter import Parser, BaseSource


def test_pandoc_json_parse():
    _source = BaseSource.init(
        url='https://github.com/python/peps.git',
        files_regexp=r'.*\.(txt|rst)$',
        format='rst'
    )
    _parser = Parser().load(_source)
