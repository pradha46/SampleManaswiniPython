
def find_second_smallest_largest(arr):
    if len(arr) < 2:
        return None, None  

    unique_arr = list(set(arr))  # Remove duplicates
    if len(unique_arr) < 2:
        return None, None 

    unique_arr.sort()
    second_smallest = unique_arr[1]
    second_largest = unique_arr[-2]

    return second_smallest, second_largest
