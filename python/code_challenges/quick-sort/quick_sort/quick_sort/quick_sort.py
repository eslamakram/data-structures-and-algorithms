def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low]= temp

def Partition(arr,left, right):
    pivot = arr[right]
    low = left -1

    for i in range(left,right):
        if arr[i]<= pivot:
            low += 1
            Swap(arr, i, low)

    Swap(arr, right, low+1)
    return low+1

def QuickSort(arr , left, right):
    if left < right:
        position = Partition(arr, left, right)

        QuickSort(arr, left, position-1)
        QuickSort(arr, position+1, right)

    return arr

if __name__ == "__main__":
    
    testArray = [8,4,23,42,16,15]
    print(f'Array: {testArray}')
    QuickSort(testArray,0,5)
    print(f'Sorted Array: {testArray}')


