array = [2,4,6,-8]
addedValue = 5


def array_insert_shift(array,addedValue):
    middleIndex = int(len(array)/2)
    result =[0]
    for i in range(middleIndex+1):
       result[i]= array[i]
       result[middleIndex]= addedValue
       for j in range(middleIndex+1,int(len(array))):
           result[j]= array[j-1]
    return result

array_insert_shift(array,addedValue)






