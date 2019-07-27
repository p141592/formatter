import pytest

from parser.term import Term
from parser.article import Article


@pytest.mark.parametrize("content,_hash", [(["test"], 8)])
def test_hash(content, _hash):
    article = Article()
    for line in content:
        term = Term()
        term.append(line)
        article.append(term)
    assert hash(article) == _hash  # Результатом должен быть хеш от хеша всех детей

