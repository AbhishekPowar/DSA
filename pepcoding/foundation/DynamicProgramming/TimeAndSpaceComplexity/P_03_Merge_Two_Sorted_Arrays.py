def mergeUsingExtraSpace(arr1, arr2):
    mergeArray = []
    len1 = len(arr1)
    len2 = len(arr2)
    idx1 = idx2 = 0

    while idx1 < len1 and idx2 < len2:
        if arr1[idx1] < arr2[idx2]:
            mergeArray.append(arr1[idx1])
            idx1 += 1
        else:
            mergeArray.append(arr2[idx2])
            idx2 += 1
    while idx1 < len1:
        mergeArray.append(arr1[idx1])
        idx1 += 1
    while idx2 < len2:
        mergeArray.append(arr2[idx2])
        idx2 += 1
    return mergeArray


def mergedTwoSortedArray(arr1, arr2):
    def insort(ar, lenOfArr):
        if lenOfArr > 1:
            key = ar[0]
            idx = 1
            while idx < lenOfArr and ar[idx] < key:
                ar[idx-1] = ar[idx]
                idx += 1
            ar[idx-1] = key

    len1 = len(arr1)
    len2 = len(arr2)
    idx1 = idx2 = 0
    while idx1 < len1 and arr1[len1-1] > arr2[0]:
        if arr1[idx1] < arr2[idx2]:
            idx1 += 1
        else:
            arr1[idx1], arr2[idx2] = arr2[idx2], arr1[idx1]
            insort(arr2, len2)
    return arr1+arr2


if __name__ == "__main__":
    arr1 = [-2, 5, 9, 11]
    arr2 = [4, 6, 8]
    arr1 = [-1, 0]
    arr2 = [0, 1]
    # n = int(input())
    # arr1 = [int(input()) for _ in range(n)]
    # m = int(input())
    # arr2 = [int(input()) for _ in range(m)]

    mergedArray = mergedTwoSortedArray(arr1, arr2)
    [print(m) for m in mergedArray]
    print('end')
