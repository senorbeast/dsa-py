#
## Kadane's Algorithm
# Overlaps with Two pointers, sliding window, greedy and DP

# Find a non-empty subarray with the largest sum
# arr = [4, -1, 2, -7, 3, 4]

# Subarray: Is a CONTIGUOUS sub collection of an array


## Brute Force

# Go over every sub array, start from 0th idx, create subarrays..

# TC: O(n^2)
# SC: O(1)


def bruteForce(nums: list[int]) -> int:
    maxSum = nums[0]

    for i in range(len(nums)):
        currSum = 0
        for j in range(i, len(nums)):
            currSum += nums[j]
            maxSum = max(maxSum, currSum)

    return maxSum


# Some what greedy, resultant is updated at every idx

# TC: O(n)
# SC: O(1)


# Code in loop can get a bit hard to read
# Since we are not using any pointers, but implicitly there is a window
# Which we keep track by currSum (max sub array sum possible at particular index)


def kadanes(nums: list[int]) -> int:
    maxSum = nums[0]
    currSum = 0

    # At every iteration, update what info is propogate and the res
    # i.e. Info propogated here, is the currSum ( maximum sum subarray at that index can give)
    # and Res is the maxSum ( max currSum, max sub array sum)
    for n in nums:
        currSum = max(currSum, 0)  # never add -ve to get maximum sum
        currSum += n
        maxSum = max(currSum, maxSum)

    return maxSum


## Kadanes' Variation (Sliding Window)

# Instead of returning max sum of subArray, return the left and right index of max subarray sum
# Assuming there is exactly one result, no ties


def slidingWindow(nums: list[int]) -> tuple:

    maxSum = nums[0]
    maxLeft, maxRight = 0, 0
    currSum = 0
    L = 0

    for R in range(len(nums)):

        # Starting new window (new subarray), when prev currSum is -ve
        # this L may not be out maxLeft, just left of currSum
        if currSum < 0:
            currSum = 0
            L = R

        currSum += nums[R]

        # Window endPos, when currSum > prev maxSum
        # We got new MaxSum, store maxLeft, maxRight
        if currSum > maxSum:
            maxSum = currSum
            maxLeft, maxRight = L, R

    return maxLeft, maxRight
