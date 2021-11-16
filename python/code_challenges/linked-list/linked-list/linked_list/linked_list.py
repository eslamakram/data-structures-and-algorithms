

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None

    def append(self,value):
      # create node and give it value and assign next pointer to none
        node = Node(value)
      #  check if linked list is empty
        if self.head is None:
           self.head = node
      # linked list is full
        else:
              currentNode = self.head
              while currentNode.next != None:
                    currentNode = currentNode.next
              currentNode.next = node


    def includes(self,value):
        include = False
        if self.head is None:
            include = False
        else:
            current = self.head
            while current is not None:
                  if current.value == value:
                      include = True
                  current = current.next
        return include




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

     print (Linked_List_test.includes(1992))

     print(Linked_List_test)



