import threading

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Create threads for sorting left and right halves
    left_thread = threading.Thread(target=lambda: sorted_left.append(threaded_merge_sort(left)))
    right_thread = threading.Thread(target=lambda: sorted_right.append(threaded_merge_sort(right)))

    sorted_left = []
    sorted_right = []

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return merge(sorted_left[0], sorted_right[0])


