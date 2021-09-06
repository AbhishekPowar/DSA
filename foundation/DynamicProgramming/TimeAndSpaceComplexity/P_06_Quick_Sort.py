def partionArrayPep(ar, low, high):
    i = low
    j = low
    pivot = ar[high]
    print(f'pivot -> {pivot}')
    pivotIndex = high
    while i <= high:
        while i <= high and ar[i] > pivot:
            i += 1
        if i <= high:
            print(f'Swapping {ar[i]} and {ar[j]}')
            ar[i], ar[j] = ar[j], ar[i]
            j += 1
            i += 1
    print(f'pivot index -> {j-1}')
    return j-1


def partionArray(ar, low, high):
    start = low
    end = high
    pivot = ar[start]
    pivotIndex = start
    while start < end:
        while start <= high and ar[start] <= pivot:
            start += 1
        while end >= 0 and ar[end] > pivot:
            end -= 1
        if start < end:
            ar[start], ar[end] = ar[end], ar[start]
    ar[pivotIndex], ar[end] = ar[end], ar[pivotIndex]
    return end


def quickSort(ar):
    def quickSortImpl(ar, low, high):
        if low < high:
            pivotIdx = partionArray(ar, low, high)
            quickSortImpl(ar, 0, pivotIdx-1)
            quickSortImpl(ar, pivotIdx+1, high)
    quickSortImpl(ar, 0, len(ar)-1)
    return ar


if __name__ == "__main__":
    ar = [7, -2, 4, 1, 3]
    # n = int(input())
    # ar = [int(input()) for _ in range(n)]
    # pivot = int(input())
    # print(ar)
    output = quickSort(ar)
    print(*output)
