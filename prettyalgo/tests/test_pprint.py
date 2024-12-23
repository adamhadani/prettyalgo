"""Unit-tests for the pprint module."""

import pytest

from prettyalgo.pprint import PrettyListPrinter


def test_pformat_empty():
    lst = []
    pprint = PrettyListPrinter()
    assert isinstance(pprint.pformat(lst), str)


def test_pformat_wrong_format():
    lst = dict(a="b")
    pprint = PrettyListPrinter()

    with pytest.raises(TypeError):
        pprint.pformat(lst)


def test_pformat_basic_list():
    lst = [0, 1, 1, 3]
    pprint = PrettyListPrinter()

    assert isinstance(pprint.pformat(lst), str)


def test_pformat_basic_tuple():
    lst = (0, 1, 1, 3)
    pprint = PrettyListPrinter()

    assert isinstance(pprint.pformat(lst), str)


def test_pformat_basic_str():
    lst = "abcdefg"
    pprint = PrettyListPrinter()

    assert isinstance(pprint.pformat(lst), str)
