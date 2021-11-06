
def array_insert_shift(array,addedValue):

    # end = len(array)
    middleIndex = len(array)//2
    # array =array + [0]
    # while end >= middleIndex:
    #    array[end]= array[end-1]
    #    end -=1

    #    array[-middleIndex]= addedValue

    result = [0]*(len(array)+1)
    for i in range( middleIndex):
        result[i] = array[i]
    result[middleIndex] = addedValue
    for j in range(middleIndex +1 , len(result)):
        result[j] = array[j -1]

    return result



if __name__ == "__main__":

  array = [2,4,6,-8]
  addedValue = 5
print(array_insert_shift(array,addedValue))






