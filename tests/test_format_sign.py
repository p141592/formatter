import pytest

from parser.parser import Parser
from tests.format_sign_test_set import FORMAT_SIGN


@pytest.mark.parametrize("line,expected", FORMAT_SIGN)
def test_sign(line, expected):
    """
    Набрать test_set, в котором лежит строки с признаком формата и без. Проверить, что отрабатывает верно
    :return:
    """
    assert Parser.check_special_symbols(line) is expected
