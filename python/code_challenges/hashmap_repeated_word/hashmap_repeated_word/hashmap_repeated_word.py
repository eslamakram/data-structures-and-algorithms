import re
from hashmap_repeated_word.linked_list import *
from hashmap_repeated_word.hashtable import *


def repeated_word(sentance=None):
    """
    Write a function called repeated word that finds the first word to occur more than once in a string
    Arguments: string
    Return: string
    """
    arr=sentance.lower().split(" ")
    hash_table=HashTable()
    if sentance == None :
        return "None"
    for  i in arr:
        if hash_table.contains(i):
            return (i, len(arr))
        hash_table.add(i,i)
    return "None"


