def findLargest(ar, k):
    def findLargestImpl(a, low, high, k):
        i = low
        j = high
        pivot = a[j]
        pivotIndex = j
        while i < j:
            while i <= high and a[i] > pivot:
                i += 1
            while j >= 0 and a[j] <= pivot:
                j -= 1
            if i < j:
                a[i], a[j] = a[j], a[i]
        i, j = j, i
        a[pivotIndex], a[j] = a[j], a[pivotIndex]
        if j == k:
            return a[k]
        elif j < k:
            findLargestImpl(a, j+1, high, k)
        else:
            findLargestImpl(a, low, j-1, k)

    N = len(ar)-1
    k -= 1
    findLargestImpl(ar, 0, N, k)
    return ar[k]


if __name__ == "__main__":
    from random import *
    ar = [7, -2, 4, 1, 3]
    k = 3
    output = findLargest(ar, k)
    print(output)
    print(f'expected output {sorted(ar,reverse=1)[k-1]}')
