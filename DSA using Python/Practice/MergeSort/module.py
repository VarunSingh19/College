def merge_sort(array):
    if len(array) > 1:
        r = len(array)//2
        l = array[:r]
        m = array[r:]

        merge_sort(l)
        merge_sort(m)
        i = j = k = 0
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1

        while i < len(l):
            array[k] = l[i]
            i +=1
            k +=1
        while j < len(m):
            array[k] = m[j]
            j +=1
            k +=1
def print_list(array):
    for i in range(len(array)):
        print(array[i], end=" ")
if __name__ == '__main__':
    array = [213,21,3, 1333 , 323131,312131,4564]
    merge_sort(array)
    print_list(array)
        
