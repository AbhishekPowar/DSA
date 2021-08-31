def bubbleSort(nums):
    numsLen = len(nums)

    for i in range(numsLen):
        for j in range(0, numsLen-1-i):
            print(f'Comparing {nums[j+1]} and {nums[j]}')
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                print(f'Swapping {nums[j]} and {nums[j+1]}')


if __name__ == "__main__":
    nums = [7, -2, 4, 1, 3]
    # count = int(input())
    # nums = [int(input()) for _ in range(count)]
    bubbleSort(nums)
    [print(n) for n in nums]
