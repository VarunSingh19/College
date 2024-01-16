def bs_recursive(array, low, high, E):
    if high >= low:
        mid = (high + low) // 2
        if array[mid] == E:
            return mid
        elif array[mid] > E:
            return bs_recursive(array, low, mid - 1, E)
        else:
            return bs_recursive(array, mid + 1, high, E)
    else:
        return -1

if __name__ == "__main__":
    array = [13, 110, 115, 120, 135, 140, 260]
    E = 115
    low = 0
    high = len(array) - 1
    index = bs_recursive(array, low, high, E)
    if index != -1:
        print("Element Found At The Array at The Index", str(index))
    else:
        print("Element Is Not Present in The Array.")
