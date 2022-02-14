# pepcoding some order related issue. GFG checked for all testcases
def insertionSort(nums):
    numsLen = len(nums)

    for i in range(1, numsLen):
        key = nums[i]
        for j in range(i-1, -2, -1):
            if j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
            else:
                break
        nums[j+1] = key


if __name__ == "__main__":
    nums = [7, -2, 4, 1, 3]
    # count = int(input())
    # nums = [int(input()) for _ in range(count)]
    insertionSort(nums)
    [print(n) for n in nums]
