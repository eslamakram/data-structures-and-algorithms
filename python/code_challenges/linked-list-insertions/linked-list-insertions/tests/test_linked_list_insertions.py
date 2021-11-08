from linked_list_insertions import __version__

from linked_list_insertions.linked_list_insertions import Node, Linked_List

import pytest

def test_version():
    assert __version__ == '0.1.0'

# Can successfully add a node to the end of the linked list
# Can successfully add multiple nodes to the end of a linked list
# Can successfully insert a node before a node located i the middle of a linked list
# Can successfully insert a node before the first node of a linked list
# Can successfully insert after a node in the middle of the linked list
# Can successfully insert a node after the last node of the linked list


# def test_add_node_linked_list():
#     ll = Linked_List()
#     expected = None
#     actual = ll.head
#     assert expected == actual

# def test_add_multiple_nodes_to_existing_ll(ll):
#     ll.append(True)
#     ll.append("Hello")
#     expected = 'Head -> 1 -> Hello -> 1991 -> 6 -> 7 -> True -> Hello -> None'
#     actual = ll.__str__()
#     assert expected == actual

# def test_insert_node_before_middle_ll(ll):
#     ll.Insert_Before_Item(1991, "Mid")
#     expected = 'Head -> 1 -> Hello -> Mid -> 1991 -> 6 -> 7 -> None'
#     actual = ll.__str__()
#     assert expected == actual


# def test_insert_node_before_first_ll(ll):
#     ll.Insert_Before_Item(1, "First")
#     expected = 'Head -> First -> 1 -> Hello -> 1991 -> 6 -> 7 -> None'
#     actual = ll.__str__()
#     assert expected == actual

# def test_insert_node_after_middle_ll(ll):
#     ll.Insert_After_Item(1991, "Mid")
#     expected = 'Head -> 1 -> Hello -> 1991 -> Mid -> 6 -> 7 -> None'
#     actual = ll.__str__()
#     assert expected == actual

# def test_insert_node_after_first_ll(ll):
#      ll.Insert_After_Item(1,"First")
#      expected = 'Head -> 1 -> First -> Hello -> 1991 -> 6 -> 7 -> None'
#      actual = ll.__str__()
#      assert expected == actual

def test_kth_From_End(ll):
    expected = 1
    actual = print( ll.kthFromEnd(5))
    assert expected == actual

@pytest.fixture
def ll():
    ll = Linked_List()
    ll.append(1)
    ll.append('Hello')
    ll.append(1991)
    ll.append(6)
    ll.append(7)
    return ll
