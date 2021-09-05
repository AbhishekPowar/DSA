def mergeSort(ar):
    def mergeArray(ar, low, mid, high):
        print('Merging these two arrays')
        i = low
        j = mid+1
        print('left array ->', *ar[low:mid+1])
        print('right array ->', *ar[j:high+1])
        c = []
        while i <= mid and j <= high:
            if ar[i] < ar[j]:
                c.append(ar[i])
                i += 1
            else:
                c.append(ar[j])
                j += 1
        c.extend(ar[i:mid+1])
        c.extend(ar[j:high+1])
        ar[low:high+1] = c[:]

    def mergeSortImpl(ar, low, high):
        if low < high:
            mid = (low + high)//2
            mergeSortImpl(ar, low, mid)
            mergeSortImpl(ar, mid+1, high)
            mergeArray(ar, low, mid, high)
    mergeSortImpl(ar, 0, len(ar)-1)
    return ar


if __name__ == "__main__":
    ar = [-2, 1, 3, 4, 7]
    n = int(input())
    ar = [int(input()) for _ in range(n)]
    output = mergeSort(ar)
    print('Sorted Array ->', *output)
