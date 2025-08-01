
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

# Example usage
sample_list = [33, 10, 68, 19, 42, 44, 11]
sorted_list = quicksort(sample_list)
print("Sorted list:", sorted_list)
