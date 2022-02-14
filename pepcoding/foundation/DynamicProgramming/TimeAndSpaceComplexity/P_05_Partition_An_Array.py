def partionArray(ar, low, high, pivot):
    start = low
    end = high
    # pivot = ar[start]
    # pivotIndex = start
    while start < end:
        while start <= high and ar[start] <= pivot:
            start += 1
        while end >= 0 and ar[end] > pivot:
            end -= 1
        if start < end:
            print(f'Swapping {ar[start]} and {ar[end]}')
            ar[start], ar[end] = ar[end], ar[start]
    # ar[pivotIndex], ar[end] = ar[end], ar[pivotIndex]
    return ar


def partionArrayPep(ar, low, high, pivot):
    i = low
    j = low
    while i <= high:
        while i <= high and ar[i] > pivot:
            i += 1
        if i <= high:
            print(f'Swapping {ar[i]} and {ar[j]}')
            ar[i], ar[j] = ar[j], ar[i]
            j += 1
            i += 1
    return ar


if __name__ == "__main__":
    ar = [1, 3, 5, 7, 2, 4, 6, 8]
    pivot = 5
    # import sys
    # sys.stdin = open('input.txt','r')

    n = int(input())
    ar = [int(input()) for _ in range(n)]
    pivot = int(input())

    output = partionArrayPep(ar, 0, len(ar)-1, pivot)
    print(*output)
