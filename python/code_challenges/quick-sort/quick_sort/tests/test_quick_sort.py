from quick_sort import __version__
from quick_sort.quick_sort import *

def test_version():
    assert __version__ == '0.1.0'


def test_quick_sort():
    arr=[8,4,23,42,16,15]
    QuickSort(arr,0,5)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_quick_sort_reversed():
    reversed_arr=[20,18,12,8,5,-2]
    QuickSort(reversed_arr,0,5)
    assert reversed_arr == [-2, 5, 8, 12, 18, 20]

def test_quick_sort_Few_uniques():
        Few_uniques=[5,12,7,5,5,7]
        QuickSort(Few_uniques,0,5)
        assert Few_uniques == [5, 5, 5, 7, 7, 12]

def test_unhappy():
    arr=[]
    QuickSort(arr,0,0)
    assert arr == []

