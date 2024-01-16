# Python3 implementation of QuickSort
# Function to find the partition position
def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j

            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1
# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)
    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")


# def Quick_Sort(arr, low, high):
#     if low < high:
#         pi =  Partition(arr, low, high)
#         Quick_Sort(arr,low, pi -1)
#         Quick_Sort(arr, pi + 1, high)
# def Partition(arr,low,high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low,high):
#         if arr[j] <= pivot:
#             i = i+1
#             (arr[i],arr[j]) = (arr[j],arr[i])
#     (arr[i+1],arr[high]) = (arr[high],arr[i+1])
#     return i + 1

# if __name__== 'main':
#     arr = [122,21,33,2,44,332,22223]
#     n = len(arr)
#     Quick_Sort(arr,0,n-1)
#     print('Sorted Array :')
#     for x in arr:
#         print(x, end=" ")
