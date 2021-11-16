
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            currentNode = self.head
            while currentNode.next != None:
                currentNode = currentNode.next
            currentNode.next = node

    def Insert_After_Item(self, item, data):
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

    def kthFromEnd(self, k):
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


def linked_list_zip(list1, list2):
    """
       ll3 = LinkedList()
    current1 = ll1.head
    current2 = ll2.head
    # ll1 head -> [1] -> [3] -> [2] -> X
    # ll2 head -> [5] -> [9] -> [4] -> X
    # head -> 1 -> 5 -> 3 -> 2-> X
    # temp -> 9 -> 4 -> X
    while (current1 or current2):
        # move every node in ll2 to be after every node in ll1
        pass
    """
    if list1.head is None:
        return str(list2)
    if list2.head is None:
        return str(list1)

    # if only one node in first list
    # simply point its head to second list
    if (list1.next == None) :
        list1.next = list2
        return str(list1)
    """
    # Initialize current and next pointers of
    # both lists
    curr1 = h1
    next1 = h1.next
    curr2 = h2
    next2 = h2.next

    while (next1 != None and curr2 != None):

        # if curr2 lies in between curr1 and next1
        # then do curr1.curr2.next1
        if ((curr2.data) >= (curr1.data) and
            (curr2.data) <= (next1.data)) :
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1

            # now let curr1 and curr2 to point
            # to their immediate next pointers
            curr1 = curr2
            curr2 = next2

        else :
            # if more nodes in first list
            if (next1.next) :
                next1 = next1.next
                curr1 = curr1.next

            # else point the last node of first list
            # to the remaining nodes of second list
            else :
                next1.next = curr2
                return h1

    return h1"""

    while (current1 or current2):
          current1 = list1.head
          current2 = list2.head
          if current1 is not None:
             current1.head = list2.head
          else:
            while current2:
                temp = current1.next
                current1.next = current2
                current2 = temp

                current1 = current1.next
                current2 = current2.next
    return (list1.__str__())


def ispalindrome(head):
    temp = head
    list2 = Linked_List()
    flag_is_palin = True
    while temp != None:
        list2.append(temp.value)
        temp = temp.next

        while head != None:
            item = temp.pop()

            if head.value == item:
                flag_is_palin = True
            else:
                flag_is_palin = False
                break
            head = head.next
    return flag_is_palin




if __name__ == "__main__":
    Linked_List_test1 = Linked_List()
    Linked_list_test2 = Linked_List()

    Linked_List_test1.append(1)
    Linked_List_test1.append(2)
    Linked_List_test1.append(2)
    Linked_List_test1.append(1)

    Linked_list_test2.append(2)
    Linked_list_test2.append(3)
    Linked_list_test2.append('eslam')

    #  print (Linked_List_test.Insert_Before_Item(1991,4))
    #  print (Linked_List_test.Insert_After_Item(1991,"Ansam"))
    #  print(Linked_List_test)
    print('this is the first list')
    print(Linked_List_test1.__str__())
    print("***********************************")
    print('this is the 2nd list')
    print(Linked_list_test2.__str__())
    print("***********************************")
    y = linked_list_zip(Linked_List_test1,Linked_list_test2)
    print(y)

    # print(ispalindrome(Linked_List_test))
