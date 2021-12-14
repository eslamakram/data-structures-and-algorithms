from tree_intersection.binary_tree import *
from tree_intersection.hash_table import *

def tree_intersection( tree1, tree2):
    '''
    function that takes two binary trees as parameters.
     Returns : array of the intersection between inputed trees
    '''
    outputList = []
    hashmap = Hash_table(1024)

    if tree1.root == None or tree2.root == None:
        return "one of tree is empty"


    def Traverse(node):
        if hashmap.contains(str(node.value)):
            nonlocal outputList
            outputList += [node.value]

        else:
            hashmap.add(str(node.value), True)

        if node.left:
            Traverse(node.left)

        if node.right:
            Traverse(node.right)


    Traverse(tree1.root)
    Traverse(tree2.root)

    return outputList


if __name__ == "__main__":
        tree1=BinaryTree()
        root1=Node_(100)
        root1.left=Node_(200)
        root1.left.left=Node_(300)
        root1.left.right=Node_(400)
        root1.right=Node_(500)
        root1.right.left=Node_(600)
        tree1.root=root1

        tree2=BinaryTree()
        root=Node_(100)
        root.left=Node_(500)
        root.left.left=Node_(1000)
        root.left.right=Node_(600)
        root.right=Node_(687)
        root.right.left=Node_(7689)
        root.right.left.left=Node_(300)

        tree2.root=root
        print(tree_intersection(tree1,tree2))



