
# linked list insertion After & Before 
<!-- Description of the challenge -->
Nov 7,2021 Sunday ... [Pull Requist](https://github.com/eslamakram/data-structures-and-algorithms/pull/27)

## Approach & Efficiency
time complexity of insertion after or before an item is O(n)

## Solution
<!-- Show how to run your code, and examples of it in action -->
def Insert_After_Item(self,item,data):
        node = self.head
        while node is not None:
            if node.value == item:
                break
            node = node.next
        if node is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node


    def Insert_Before_Item(self, item, data):
        if self.head is None:
            print("List has no element")
            return

        if item == self.head.value:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        print(current_node.next)
        while current_node.next is not None:
            if current_node.next.value == item:
                break
            current_node = current_node.next
        if current_node.next is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node


### Task and Test specification 

- [x] add a node to the end of the linked list
- [x] add multiple nodes to the end of a linked list
- [x] insert a node before a node located i the middle of a linked list
- [x] insert a node before the first node of a linked list
- [x] insert after a node in the middle of the linked list
- [x] insert a node after the last node of the linked lis

