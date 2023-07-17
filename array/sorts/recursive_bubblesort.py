def recursive_bubblesort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
    return recursive_bubblesort(array[:n - 1]) + [array[n - 1]]