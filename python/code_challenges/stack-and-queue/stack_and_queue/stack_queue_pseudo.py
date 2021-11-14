from stack_and_queue import  Stack

class PseudoQueue:
      def __init__(self):
          self.Push_Stack = Stack()
          self.Pop_Stack = Stack()

      def enqueue(self,value):
        self.Push_Stack.push(value)

      def dequeue(self):
         if self.Pop_Stack.is_empty():
            while self.Push_Stack.top != None:
                  self.Pop_Stack.push(self.Push_Stack.pop())
         return (self.Pop_Stack.pop())

if __name__ == "__main__":
    testQueue=PseudoQueue()
    testQueue.enqueue(1991)
    testQueue.enqueue(1)
    testQueue.enqueue(1)
    testQueue.enqueue("Tolay")
    print(testQueue.dequeue())
    print(testQueue.dequeue())
    print(testQueue.dequeue())
