def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n - 1):
        flag = 0  # A flag to check if any swaps are made in the current pass.
        for j in range(n - 1 - i):  # The inner loop goes from the first element to the unsorted boundary.
            if sequence[j] > sequence[j + 1]:
                # If the current element is greater than the next element, swap them.
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
                flag = 1  # Mark the flag as 1 to indicate that a swap occurred.

        if flag == 0:
            # If no swaps occurred in the current pass, the array is already sorted, so we can stop early.
            break

    return sequence  # Return the sorted sequence after all passes are done.

arr = [12, 33, 123, 2, 31, 21]
a = bubble_sort(arr)
print(a)
