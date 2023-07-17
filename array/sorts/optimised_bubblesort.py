def optimised_bubble_sort(array):
    for i in range(len(array)-1):
        swapped = False
        for j  in range(len(array-1-i)):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
            if not swapped:
                return array
    return array