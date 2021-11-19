
from stack_and_queue.stack_and_queue import Stack
from stack_and_queue.stack_queue_brackets import Multi_Bracket_Validation

def test_multi_brackets_1():
    expected = True
    actual = Multi_Bracket_Validation('{}{Code}[Fellows](())')
    assert expected == actual

def test_multi_brackets_2():
    expected = False
    actual = Multi_Bracket_Validation('[({}]')
    assert expected == actual

def test_multi_brackets_3():
    expected = False
    actual = Multi_Bracket_Validation('{(})')
    assert expected == actual


def test_multi_brackets_4():
    expected = True
    actual = Multi_Bracket_Validation('(){}[[]]')
    assert expected == actual


def test_multi_brackets_5():
    expected = True
    actual = Multi_Bracket_Validation('()[[Extra Characters]]')
    assert expected == actual
