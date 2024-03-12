def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):  
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [121,32,3,2,424,2421,1212,12]
    print("Name: Varun Singh\nClass: SYBSC CS\nRoll no: 999")
    print("Given Array is: ", end="\n")
    print_list(arr)
    merge_sort(arr)
    print("Sorted Array is: ", end="\n")
    print_list(arr)
