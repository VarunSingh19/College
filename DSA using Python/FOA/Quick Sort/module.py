def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
# Driver Code
if __name__ == '__main__':
    input_list = [12,3,444,554,43,222]
    sorted_list = quick_sort(input_list)

    print("Name: Varun Singh\nClass: SYBSC CS\nRoll no: 999")
    print("Original List :", input_list)
    print("Sorted List :",sorted_list)