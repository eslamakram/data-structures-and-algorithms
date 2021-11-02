
def binary_search(array1, searchKey):
    start = 0
    end = len(array1) - 1
    while(start <= end):
        mid = (start + end) // 2
        if(array1[mid] > searchKey):
            end = mid - 1
        elif(array1[mid] < searchKey):
            start = mid + 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    print(binary_search([11, 23, 36, 47, 51, 66, 73, 83, 92],23))
