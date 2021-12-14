
from tree_intersection import __version__

from tree_intersection.binary_tree import *
from tree_intersection.hash_table  import *
from tree_intersection.tree_intersection import *



def test_version():
    assert __version__ == '0.1.0'



def test_tree_intersection():
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

    assert tree_intersection(tree1,tree2)==[100,500,600,300]


def test_tree_intersection_if_no_common():
    tree1=BinaryTree()
    root1=Node_(10570)
    root1.left=Node_(20089)
    root1.left.left=Node_(30980)
    root1.left.right=Node_(49800)
    root1.right=Node_(50890)
    root1.right.left=Node_(60090)
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

    assert tree_intersection(tree1,tree2)==[]
