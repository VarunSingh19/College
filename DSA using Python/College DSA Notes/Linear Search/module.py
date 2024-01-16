# Linear search to find an element in an array

# Example 1
# def linear_search(array, target):
#     for index in range(len(array)):
#         if array[index] == target:
#             return index
#     return -1

# if __name__ == "__main__":
#     array = [2, 8, 15, 3, 7, 10]
#     target_element = 7

#     index = linear_search(array, target_element)
#     if index != -1:
#         print("Element found at index:", index)
#     else:
#         print("Element not found in the array.")

def linear_search(array,target):
    for index in range(len(array)):
        if array[index]==target:
            return index
    return -1

if __name__ == "__main__":
    array = [3,1,14,423,232,322,56]
    target_element = 423
    index = linear_search(array,target_element)
    if index != -1:
        print('element found at index' , index)
    else:
        print('element not exist.') 



# Example 2.
def Example_Two():
    print("Enter 10 Number")
    arr = []
    for i in range(10):
        arr.insert(i,int(input()))

    print("Enter The Number To Search :")
    num= int(input())
    for i in range(10):
        if num==arr[i]:
            index = i
            break
    print("Number Found at Index :", index)

# call below function to run.
# Example_Two()

def exampleTwo():
    print("Enter The Number Of Element. (Ex :10 )")
    arr = []
    for i in range(10):
        arr.insert(i,int(input()))

    print("Enter The Number To Search :")
    num = int(input())
    for i in range(10):
        if num == arr[i]:
            index = i
            break
    print("Number Found At Index :", index)

# exampleTwo()

#
#  Example 3:

def Example_Three():
    print("Enter The Size")
    arr_size = int(input())
    print("Enter " + str(arr_size) + " Elements")
    arr = []
    for i in range(arr_size):
        arr.append(input())

    print("Enter The Number To Search:")
    element = input()
    check = 0
    for i in range(arr_size):
        if element == arr[i]:
            index = i
            check = 1
            break
    if check == 1:
        print("Number Found at Index:", str(index))
    else:
        print("Not Found In Array")



# Example_Three()






