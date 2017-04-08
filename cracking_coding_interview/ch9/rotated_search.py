def rotation_search(array, start, end, val):
    # base case
    mid = (start + end) / 2
    if array[mid] == val:
        final = mid
    # inductive step
    else:
        if val < array[mid]:
            if mid == 0:
                size = len(array)
                new_mid = size / 2
                final = rotation_search(array, start, new_mid + 1, val)
            else:
                final = rotation_search(array, start, mid - 1, val)
        else:
            if mid == end:
                size = len(array)
                new_mid = size / 2
                final = rotation_search(array, 0, new_mid - 1, val)
            else:
                final = rotation_search(array, mid + 1, end, val)
    return final


if __name__ == '__main__':
    result = rotation_search([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 0, 11,
                             7)
    print(result)
