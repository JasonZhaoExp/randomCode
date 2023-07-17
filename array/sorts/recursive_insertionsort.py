def recursive_insertionsort(array):
    n = len(array)
    if n <= 1:
        return
    recursive_insertionsort(array, n - 1)
    key = array[n - 1]
    j = n - 2
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key