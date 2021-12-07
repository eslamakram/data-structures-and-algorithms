def insertion_sort(array_list):
    for i in range(1, len(array_list)):

        j = i - 1
        temp = array_list[i]

        while j >= 0 and temp < array_list[j]:
            array_list[j + 1] = array_list[j]
            j = j - 1

        array_list[j+1] = temp
