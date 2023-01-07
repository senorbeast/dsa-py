#
## Sliding Window  Fixed


# Given an array, return True if there are 2 elements within a window of size k, which are equal
# k = 2
# arr = [1,2,3,2,3,3]


# Brute Force, Sliding Window
## Allow windows less than k, so L should go till 2nd last index whatever the window size maybe

# TC: O(n*k)
# SC: O(1)
def slidingWinF(arr: list[int], k: int) -> bool:
    for L in range(len(arr)):
        for R in range(L + 1, min(len(arr), L + k)):  # to keep in range
            if arr[L] == arr[R]:
                return True

    return False


# Detect duplicates
# Using a rolling Hashset ? to memoize
# Instead of looping through the window, we store current window in Hashset, compare with new rights

# TC: O(n)
# SC: O(k)
def slidingWinFixed(nums: list[int], k: int) -> int:

    window = set()  # cur window size <= k
    L = 0

    for R in range(len(nums)):

        # Shifting L, remove
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1

        # If num already in window
        if nums[R] in window:
            return True

        window.add(nums[R])
    return False
