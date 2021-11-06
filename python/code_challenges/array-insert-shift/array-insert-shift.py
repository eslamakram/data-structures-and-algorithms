
def array_insert_shift(array,addedValue):

    end = len(array)
    middleIndex = len(array)//2 +1
    array =array + [0]
    while end >= middleIndex:
       array[end]= array[end-1]
       end -=1

       array[-middleIndex]= addedValue

    return array


  
if __name__ == "__main__":

  array = [2,4,6,-8]
  addedValue = 5
print(array_insert_shift(array,addedValue))






