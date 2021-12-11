from types import new_class
from linked_list import LinkedList

class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.map = [None]*self.size

    def hash(self, key:str) -> int:
            '''
            Hash function will hashed the key means convert the key string into a value of int
            parameters:
            key: a string
            Arguments: key
            Returns: Index in the collection for that key
            '''
            sum_of_asccii = 0
            for ch in key:
                asccii_of_ch = ord(ch)
                sum_of_asccii+= asccii_of_ch
            temp_value = sum_of_asccii*19
            hashed_key = temp_value%self.size
            return hashed_key

    def add(self, key, value):
            '''
            add a value to the hashtable by its key
            parameters:
            Arrgument: key and value
            key: a string
            value: any type
            Returns: nothing
            '''
            hashed_key = self.hash(key)

            if not self.map[hashed_key]:
                self.map[hashed_key] = value
            else:
                if isinstance(self.map[hashed_key], LinkedList):
                    self.map[hashed_key].add([key,value])
                else:
                    chain = LinkedList()
                    existing_pair = self.map[hashed_key]
                    new_pair =[key,value]
                    self.map[hashed_key]=chain
                    chain.add(existing_pair)
                    chain.add(new_pair)

    def get_value(self, key):
        hashed_key=self.hash(key)
        return self.map[hashed_key]

    def find(self,key):
        """this function will search in the hashtable about the key and return the value
        parameters:
        key: a string
        return: the value
        """
        index = self.hash(key)
        if self.map[index]:
                cuurrent=self.map[index].head
                while cuurrent:
                    if cuurrent.value[0]==key:
                        print(cuurrent.value[1])
                        return cuurrent.value[1]
                    cuurrent=cuurrent.next
        else:
            return None


    def contains(self,key):
        """this function will check if the there is a value for the key
        parameters:
        key: a string
        return: a boolean
        """
        index=self.hash(key)
        if self.map[index]:
            return self.map[index].includes(key)
        else:
            return False

if __name__ == "__main__":
    hashtable= HashTable()
    hashtable.add("TOLAY",19-2-2018)
    hashtable.add("WATEEN",5-5-2019)
    hashtable.add("eslam",1-1-1991)


    for index,item in enumerate(hashtable.map):
        if item:
            print(index, item)


    # 299 -2001
    # 396 -2019
    # 854 -1991
