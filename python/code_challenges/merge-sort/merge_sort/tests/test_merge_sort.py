from merge_sort.merge_sort.sortMerge import Mergesort, __version__
def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort():
    arr=[8,4,23,42,16,15]
    Mergesort(arr)
    assert  arr == [4, 8, 15, 16, 23, 42]

def test_merge_sort_reversed():
    reversed_arr=[20,18,12,8,5,-2]
    Mergesort(reversed_arr)
    assert   reversed_arr == [-2, 5, 8, 12, 18, 20]

def test_merge_sort_Few_uniques():
        Few_uniques=[5,12,7,5,5,7]
        Mergesort(Few_uniques)
        assert Few_uniques == [5, 5, 5, 7, 7, 12]

def test_unhappy():
    arr=[]
    Mergesort(arr)
    actual=arr
    expected=[]
    assert actual==expected
