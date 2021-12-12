# Challenge Summary

Write a function called repeated word that finds the first word to occur more than once in a string

## Whiteboard Process

![repeated_word](/hashmap-repeated-words-whiteBoard.jpg)

## Approach & Efficiency

+ Ceate function take a string with multible words
+ check if the string is empty
+ declear hashtable
+ split all the string to array contain words and chnage it to lower case and remove all marks
+ loop along the words fo each word check if the hashtable contarin the word or not if it is return the word else add the word to the hashtable

### Complexity

Time Complexity :  O(n)
space Complexity : O(n)

## Solution

[Code](hashmap_repeated_word/hashmap_repeated_word.py) | [Test](tests/test_hashmap_repeated_word.py)
