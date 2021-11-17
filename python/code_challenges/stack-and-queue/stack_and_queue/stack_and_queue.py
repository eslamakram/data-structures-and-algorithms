
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Empty():
      pass

class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        """
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance
        """
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        """
        Arguments: none
        Returns: the value from node from the top of the stack
        Removes the node from the top of the stack
        Should raise exception when called on empty stack
        """
        if self.top == None:
            raise Empty("This stack is empty")
        temp =self.top
        self.top=self.top.next
        temp.next=None
        return temp.value


    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the top of the stack
        Should raise exception when called on empty stack
        """
        if self.top == None:
            raise Exception("This stack is empty")
        return self.top.value

    def is_empty(self):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        """
        if self.top == None:
           return True
        return False

    def __str__(self):
        # "head -> 1 -> 2 -> 3 -> 4 -> None"
        output = "Head -> "
        if self.top is None:
            output += None

        else:
            current = self.top
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
            return output

    def max_push(self,value):
        """
        Arguments: value
        """
        if self.top == None:
           self.push(value)
        if value > self.peek():
            self.pop()
            self.push(value)



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self,value):
        """
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        node = Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if not self.front :
            raise Exception('Queue is Empty')
        else:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        """
        if not self.front:
            raise Exception('Queue is empty...')
        return self.front.value

    def is_empty(self):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        """
        if not self.front:
            return True
        return False

if __name__ == "__main__":
   maxStack = Stack()
   maxStack.max_push(10)
   maxStack.max_push(5)
   maxStack.max_push(2)
   print( maxStack.__str__())

