# Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->
implement and test singly linked list

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
The time complexity for initializing  singly linked list is O(1). The space complexity is O(1) as no additional memory is required to initialize the linked list.
But, for insertion at the end, the time complexity is O(N) as we need to traverse to the last element. The space complexity O(1) because it takes a constant space to add a new node.
The time complexity for searching a given element in the linked list is O(N) as we have to loop over all the nodes and check for the required one. The space complexity is O(1) as no additional memory is required to traverse through a linked list and perform a search.

## API
<!-- Description of each method publicly available to your Linked List -->
 append method : to insert value to new node and assign next to null
 includes method :  takes a value to search in list and retrun true / false if it exist or not
 string method : to print out linked list

### Implementation: Singly Linked Lists

- [x] Create a Node class
- [x] Create a Linked List class
- [x] insert Method
- [x] includes Method
- [x] print to string Method
- [x] test am empty linked list
- [x] test insert value
- [x] test includes in value in linked list
- [x] test result as print returned
