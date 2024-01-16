def merge_sort(array):
    # Base case: If the array has only one element or is empty, it is already sorted.
    if len(array) > 1:
        # Divide the array into two halves.
        r = len(array) // 2
        L = array[:r]  # Left half
        M = array[r:]  # Right half

        # Recursively call merge_sort on both halves.
        merge_sort(L)
        merge_sort(M)

        # Merge the two sorted halves.
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i] <= M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # Check if there are any remaining elements in the left and right halves.
        # Append any remaining elements to the merged array.
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def print_list(array):
    # Helper function to print the elements of the array.
    for i in range(len(array)):
        print(array[i], end=" ")

if __name__ == "__main__":
    array = [33, 343, 554, 12, 1, 442, 5332, 54]
    merge_sort(array)
    print_list(array)
