
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def append (self,value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.next != None:
                  currentNode = currentNode.next
            currentNode.next = node



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

    def kthFromEnd(self,k):
        current = self.head
        # Index of current node
        count = 0

        # Loop while end of linked list is not reached
        while (current.next is not None):
            if (count == k):
                current = current.next
                count += 1
                return current.value
            elif count > k:
                 print('Location is out of the length of LinkedList')


    def __str__(self):
        # "head -> 1 -> 2 -> 3 -> 4 -> None"
        output = "Head -> "
        if self.head is None:
            output += None

        else:
            current = self.head
            while current:
                output += f"{current.value} -> "
                current = current.next

            output += "None"
            return output




if __name__ == "__main__":
     Linked_List_test = Linked_List()

     Linked_List_test.append(1)
     Linked_List_test.append(1)
     Linked_List_test.append(1991)
     Linked_List_test.append("welcome")

     print (Linked_List_test.Insert_Before_Item(1991,4))
     print (Linked_List_test.Insert_After_Item(1991,"Ansam"))


     print(Linked_List_test)




