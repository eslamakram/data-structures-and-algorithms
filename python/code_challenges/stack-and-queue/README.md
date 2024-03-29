# Stack and Queue

A stack  order is First In Last Out (FILO).

A Queue order is First In First Out (FIFO)

## Challenge

Implementation Stack and Queue

**Stack: Create a Stack class that has a top property.**
the methods include stack class:

1. push
    Arguments: value
    adds a new node with that value to the top of the stack with an O(1) Time performance.
2. pop
    Arguments: none
    Returns: the value from node from the top of the stack
    Removes the node from the top of the stack Should raise exception when called on empty stack
3. peek
    Arguments: none
    Returns: Value of the node located at the top of the stack
    Should raise exception when called on empty stack
4. is empty
    Arguments: none
    Returns: Boolean indicating whether or not the stack is empty.

**Queue: Create a Queue class that has a front property.**
the methods include Queue class:

1. enqueue
    Arguments: value
    adds a new node with that value to the back of - the queue with an O(1) Time performance.
2. dequeue
    Arguments: none
    Returns: the value from node from the front of the queue
    Removes the node from the front of the queue
    Should raise exception when called on empty queue
3. peek
    Arguments: none
    Returns: Value of the node located at the front of the queue
    Should raise exception when called on empty stack
4. is empty
    Arguments: none
    Returns: Boolean indicating whether or not the queue is empty

### Approach & Efficiency

all methods in stack and queue take O(1)

#### API

Pull Rquest : <https://github.com/eslamakram/data-structures-and-algorithms/pull/31>

## Stack-queue-pseudo challange

### Whiteboard Process

![CH11](CH11.png)

#### Approach & Efficiency

defind class called PseudoQueue
i used two stacks as an input, to create the Queue.
The complixity of time O(1) and space O(1) for Enqueue
The complixity of time O(n) and space O(n) for Dequeue

## stack-queue-animal-shelter challange

### Whiteboard Process

![CH12](ch12.drawio.png)
#### Approach & Efficiency

Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.
i used two queues one for cat and another one for dog
The complixity of time O(1) and space O(1) for Enqueue
The complixity of time O(n) and space O(n) for Dequeue

## stack-queue-brackets challange

### Whiteboard Process

![CH13](ch13.drawio.png)

#### Approach & Efficiency

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}
i used stack as test opening and closing brackets
The complixity of time O(n) and space O(1)

## stack-max challange

### Whiteboard Process

![CH14](ch14.drawio.png)

### Approach & Efficiency

 write a ‘Max Stack’ which is defined as a Stack with an additional getMax() member function which returns the ‘biggest’ element in the Stack.
The complixity of time O(1) and space O(1)
