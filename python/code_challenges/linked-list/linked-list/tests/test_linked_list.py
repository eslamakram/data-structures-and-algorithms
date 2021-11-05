from linked_list import __version__

from linked_list.linked_list import Node, Linked_List

import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_empty_linked_list():
    ll = Linked_List()
    expected = None
    actual = ll.head
    assert expected == actual


def test_append():
    ll = Linked_List()
    ll.append(1)
    ll.append('Hello')
    ll.append(1991)
    expected = 'Head -> 1 -> Hello -> 1991 -> None'
    actual = ll.__str__()
    assert expected == actual


def test_append_to_existing_ll(ll):
    ll.append(True)
    expected = 'Head -> 1 -> Hello -> 1991 -> True -> None'
    actual = ll.__str__()
    assert expected == actual

def test_includes_in_ll(ll):
    excepted = True
    actual = ll.includes(1991)
    assert excepted == actual


def test_includes_in_ll(ll):
    excepted = False
    actual = ll.includes(199)
    assert excepted == actual


@pytest.fixture
def ll():
    ll = Linked_List()
    ll.append(1)
    ll.append('Hello')
    ll.append(1991)
    return ll
