def name():
    return "Recursive bubble sort"

def sort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    return sort(array[:n - 1]) + [array[n - 1]]