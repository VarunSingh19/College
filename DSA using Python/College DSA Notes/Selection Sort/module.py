def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current element is the minimum
        min_index = i
        for j in range(i + 1, n):
            # Find the index of the smallest element in the remaining list
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print(my_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
