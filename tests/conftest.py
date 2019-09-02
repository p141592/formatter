import os
import subprocess

import pytest

from formatter import BaseSource, Parser, Root, Document, Block, Line


def monkey_patch_fetch_files(self):
    mock_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'git_repo_mock.tar.gz')
    subprocess.run(["tar", "xvfz", f"{mock_path}", "--directory", self.get_source_path()])


@pytest.fixture
def root():
    return Root()


@pytest.fixture
def document():
    def wrap(root=None):
        if root:
            return root.create_child(child_type=Document)
        return Document()

    return wrap


@pytest.fixture
def block():
    def wrap(document=None):
        if document:
            return document.create_child(child_type=Block, content='Block')
        return Block()

    return wrap


@pytest.fixture
def line():
    def wrap(
            block=None,
            content=None,
            line_number=0
    ):
        kwargs = dict(
            content=content,
            line_number=line_number
        )
        if block:
            return block.create_child(child_type=Line, **kwargs)
        return Line(**kwargs)

    return wrap


@pytest.fixture
def small_tree(root, document, line, block):
    tree = root
    _document = document(root=tree)
    _block = block(document=_document)
    line(block=_block, line_number=1, content='Line1')
    line(block=_block, line_number=2, content='Line2')
    return tree
