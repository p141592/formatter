import pytest

from parser.term import Tree


@pytest.mark.parametrize("content,_hash", [(["test"], 1516901269977571296)])
def test_hash(content, _hash):
    term = Tree()
    for line in content:
        term.append(line)
    assert hash(term) == _hash

