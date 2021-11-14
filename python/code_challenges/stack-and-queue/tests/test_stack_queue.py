
from stack_and_queue.stack_and_queue import Node, Stack, Queue
import pytest

def test_push_stack(stack):
    actual=stack.top.value
    expected="1991"
    assert expected == actual

def test_push_multiple_stack(stack):
    stack.push('hello')
    stack.push('python')
    actual=stack.top.value
    expected="python"
    assert expected == actual

def test_empty_stack(stack):
    while stack.top:
        stack.pop()
    actual = stack.is_empty()
    expected = True
    assert expected == actual

def test_pop_stack(stack):
    actual = stack.pop()
    expected = "1991"
    assert expected == actual

def test_peek_stack(stack):
    actual = stack.peek()
    expected = "1991"
    assert expected == actual


def test_stack_pop_from_empty():
    with pytest.raises(Exception):
        stack = Stack()
        actual = stack.pop()

def test_stack_peek_from_empty():
    with pytest.raises(Exception):
        stack = Stack()
        actual = stack.peek()

# **********************************************************
# *********************QUEUE TEST***************************
# **********************************************************

def test_enqueue_queue():
     queue_test = Queue()
     queue_test.enqueue(1)
     actual = queue_test.rear.value
     expected = 1
     assert actual == expected

def test_enqueue_multiple_queue(queue):
    actual = queue.rear.value
    expected = 55
    assert actual == expected

def test_dequeue_queue(queue):
    expected = '1.1.1991'
    actual = queue.dequeue()
    assert expected == actual

def test_peek_queue(queue):
    expected = '1.1.1991'
    actual = queue.peek()
    assert expected == actual

def test_empty_queue(queue):
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert expected == actual

def test_empty_instantiate_queue():
    queue = Queue()
    expected = None
    actual = queue.front
    assert expected == actual

def test_queue_dequeue_from_empty():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.dequeue()

def test_queue_peek_from_empty():
    with pytest.raises(Exception):
        queue = Queue()
        actual = queue.peek()

@pytest.fixture
def stack():
            stack = Stack()
            stack.push(1)
            stack.push(2)
            stack.push(3)
            stack.push('1991')
            return stack

@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue('1.1.1991')
    queue.enqueue('eslam')
    queue.enqueue(55)
    return queue
