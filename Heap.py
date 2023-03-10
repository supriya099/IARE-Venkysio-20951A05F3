def heapify(arr, n, i):
    """
    Helper function to heapify a subtree rooted with node i which is
    an index in arr[]. n is size of heap
    """
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l
 
    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r
 
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)
 
 
def heap_sort(arr):
    """
    Function to perform heap sort on the given integer array arr
    """
    n = len(arr)
 
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)
 
    return arr
 
 
# Example usage
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array is:", sorted_arr)
