### Search for sorted stuff.

# Binary Search says my guess is mid value, if not adjust the window, update mid value and go on.
# Every adjustment of window/ 1 step, we divide our arr into half.

# Eg. Dictionary, Sorted Array, Sorted LL

# Binary Search

# Take the middle value of sorted array, and compare it with the target value.
# We divide the search array in half at each step.

# Taking 2 Boundaries, and finding the middle value.

#%%


def binarySearch(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    # Loop till boundaries are proper
    while left <= right:

        # Set Mid as ~ avg os left right
        mid = (right + left) // 2

        # Change Left/right boundary depending on comparision
        if target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1

        # If match return mid
        else:
            return mid
    # After search space is exhausted, no match found.
    return -1


# After each step, half of the arr is eliminated.

# X no. of steps required to divide the array to get singular element
# n/(2**x) = 1
# 2**x = n
# x = logn         (base 2)

# logn is the number of steps required to reach 1 ele
# Operations done on each step is O(c) = O(1)

# Total Time Complexity: O(logn)


# %%
arr = [0, 1, 3, 4, 4, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 2))

# %%
