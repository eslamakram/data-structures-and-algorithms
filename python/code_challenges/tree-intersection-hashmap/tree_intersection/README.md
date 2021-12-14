# Challenge Summary

Find the intersection of two trees using a hashmap, we built a hash map of tree so that our searching becomes faster and all elements appear only once.

## Whiteboard Process

![hasmap_tree_intersection](/code-challenge-32.jpg)

## Approach & Efficiency

the approach used to solve this challenge is recursion to traverse over
the tree use depth first then append the common values.

+ Ceate function take 2 tree as input
+ declear empty arr
+ decleat hash_table
+ check if the tree is empty ===> return massge
+ declear travrse function take node as input
+ check if the hash_table contains the node.value ===> add the value to the array
+ else: add the value to the hash_table
+ if there is node.left ===> call recursive node.left
+ if there is node.right===> call recursive node.right
+ Call travers with root tree1 and tree2
+ return arr

## Complexity

+ Time o (n)
+ space o(n)

## Solution

[CODE](tree_intersection/tree_intersection.py) | [TEST](tests/test_tree_intersection.py)
