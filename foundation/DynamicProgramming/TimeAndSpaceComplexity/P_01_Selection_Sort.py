def selectionSort(nums):
    numsLen = len(nums)

    for i in range(numsLen-1):
        minimum = i
        for j in range(i+1, numsLen):
            print(f'Comparing {nums[j]} and {nums[minimum]}')
            if nums[minimum] > nums[j]:
                minimum = j
        print(f'Swapping {nums[i]} and {nums[minimum]}')
        nums[i], nums[minimum] = nums[minimum], nums[i]


if __name__ == "__main__":
    nums = [7, -2, 4, 1, 3]
    # count = int(input())
    # nums = [int(input()) for _ in range(count)]
    selectionSort(nums)
    [print(n) for n in nums]
