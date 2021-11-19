from stack_and_queue.stack_queue_animal_shelter import AnimalShelter



import pytest

def test_AnimalShelter_enqueue_cat():
    expected="cat"
    animal=AnimalShelter()
    animal.enqueue("cat")
    actual=animal.cat.rear.value
    assert expected==actual

def test_AnimalShelter_enqueue_dog():
    expected="dog"
    animal=AnimalShelter()
    animal.enqueue("dog")
    actual=animal.dog.rear.value
    assert expected==actual

def test_AnimalShelter_enqueue_frog():
    with pytest.raises(Exception):
     animal=AnimalShelter()
     animal.enqueue("frog")

#@pytest.mark.skip('todo')
def test_AnimalShelter_dequeue_cat():
    animal=AnimalShelter()
    animal.enqueue("catTolay")
    animal.enqueue("catWateen")
    animal.dequeue("catTolay")
    actual=animal.cat.front.value
    expected="catWateen"
    assert expected==actual

# @pytest.mark.skip('todo')
def test_AnimalShelter_dequeue_dog():
    expected="dogTolay"
    animal=AnimalShelter()
    animal.enqueue("dogWateen")
    animal.enqueue("dogTolay")
    animal.dequeue("dogWateen")
    actual=animal.dog.front.value
    assert expected==actual



