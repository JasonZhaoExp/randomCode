def iterative_mergesort(arr):
    current_size = 1
    while current_size < len(arr) - 1:
        left = 0
        while left < len(arr) - 1:
            mid = min((left + current_size - 1), (len(arr) - 1))
            right = ((2 * current_size + left - 1,
                      len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])
            arr[left:right + 1] = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
            left = left + current_size * 2
        current_size = 2 * current_size
    return arr

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result