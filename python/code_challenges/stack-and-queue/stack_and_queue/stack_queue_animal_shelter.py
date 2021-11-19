from stack_and_queue.stack_and_queue import Queue
class AnimalShelter:
    def __init__(self) -> None:
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):
        """
        Arguments: animal
        animal can be either a dog or a cat object.
        """
        if animal.lower().startswith('cat') :
           self.cat.enqueue(animal)

        elif animal.lower().startswith('dog') :
           self.dog.enqueue(animal)

        else :
             raise Exception("The animal not in the shelf")

    def dequeue(self, pref):
        """
        Arguments: pref
        pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
        If pref is not "dog" or "cat" then return null.
        """
        if pref.lower().startswith('cat') and self.cat.front:
           return self.cat.dequeue()

        if pref.lower().startswith('dog')  and self.dog.front:
          return self.dog.dequeue()

        if pref =='dog' or pref =='cat':
           return 'The animal not there'
        else :
          return 'The animal not in the shelf'

