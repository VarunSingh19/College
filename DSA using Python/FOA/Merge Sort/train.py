# def Merge_Sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         Larray = arr[:mid]
#         Rarray = arr[mid:] 

#         Merge_Sort(Larray)
#         Merge_Sort(Rarray)


#         i = j = k = 0
#         while i< len(Larray) and j <len(Rarray):
#             if Larray[i] < Rarray[j]:
#                 arr[k] = Larray[i]
#                 i +=1
#             else:
#                 arr[k] = Rarray[j]
#                 j += 1
#             k += 1
#         while i < len(Larray):
#             arr[k] = Larray[i]
#             i += 1
#             k += 1

#         while j < len(Rarray):
#             arr[k] = Rarray[j]
#             j += 1
#             k += 1
# # if __name__ == '__main__':
# arr = [5,7,3,2,1,4,9,8,10,6]
# print('Unsorted Array \n',arr)
# Merge_Sort(arr)
# print('Sorted Array \n',arr)                                    
                    


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         Larray = arr[:mid]
#         Rarray = arr[mid:]

#         merge_sort(Larray)
#         merge_sort(Rarray)

#         i = j = k = 0

#         while i < len(Larray) and j < len(Rarray): 
#             if Larray[i] < Rarray[j]:
#                 arr[k] = Larray[i]
#                 i += 1
#             else:
#                 arr[k] = Rarray[j]
#                 j += 1
#             k += 1

#         while len(Larray) > i:
#             arr[k] = Larray[i]
#             i += 1
#             k += 1   
#         while len(Rarray) > j:
#             arr[k] = Rarray[j]
#             j += 1
#             k += 1
# arr =  [5,7,3,2,1,4,9,8,10,6]
# merge_sort(arr)
# print(arr)


# Dry Run
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid =  len(arr) // 2
#         Larray = arr[:mid]
#         Rarray = arr[mid:]

#         merge_sort(Rarray)
#         merge_sort(Larray)

#         i = j = k = 0
#         while len(Larray) > i and len(Rarray) > j:
#             # while left side and right side array is greater than 0 
#             if Larray[i] < Rarray[j]:
#                 # if array of left side is less than array of right side 
#                 arr[k] = Larray[i]
#                 # put that lesser element in the new array 
#                 i += 1
#             else:
#                 arr[k] = Rarray[j]
#                 # else if the array of right is is smaller than the left side then 
#                 # put that lesser element in the new array
#                 j += 1
#             k += 1

#         while len(Larray) > i:
#             arr[k] = Larray[i]
#             i += 1
#             k += 1
#         while len(Rarray) > j:
#             arr[k] = Rarray[j]
#             j += 1
#             k += 1
# arr = [121,32,3,2,424,2421,1212,12]
# merge_sort(arr)
# print(arr)



# def merge_sort_done(arr):
#     if len(arr) > 1 :
#         mid  = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort_done(L)
#         merge_sort_done(R)

#         i = j = k = 0

#         while len(L) > i and len(R) > j:
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while len(L) > i:
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while len(R) > j:
#             arr[k] = R[j]
#             j += 1
#             k += 1
# arr = [121,32,3,2,424,2421,1212,12]
# merge_sort_done(arr)
# print(arr)

# Hack to remember this shit...
# while len->arr->ele
# 2*while len->ele 

# Warm Up
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while len(L) > i and len(R) > j:
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while len(L) > i:
            arr[k] = L[i]
            i += 1
            k += 1
        while len(R) > j:
            arr[k] = R[j]
            j += 1
            k += 1
arr = [121,32,3,2,424,2421,1212,12]
merge_sort(arr)
print(arr)
