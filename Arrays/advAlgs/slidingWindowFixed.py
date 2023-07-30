#
## Sliding Window  Fixed


# Given an array, return True if there are 2 same elements within a window of size k, which are equal
# k = 2
# arr = [1,2,3,2,3,3]


# Brute Force, Sliding Window
## Allow windows less than k, so L should go till 2nd last index whatever the window size maybe
# Thus, it very inefficient

# TC: O(n*k)
# SC: O(1)
def slidingWinFixedBruteForce(arr: list[int], k: int) -> bool:
    for L in range(len(arr)):
        for R in range(L + 1, min(len(arr), L + k)):  # to keep in range
            if arr[L] == arr[R]:
                return True

    return False


# Detect duplicates
# Using a rolling Hashset ? to memoize
# Instead of looping through the window, we store current window in Hashset, compare with new rights

## Sliding window really depend on rolling hashset,
## in this example, comparision are made way faster because of hashset.

# # Thanks to rolling hashset.

# TC: O(n)
# SC: O(k)
def slidingWinFixed(nums: list[int], k: int) -> int:

    window = set()  # cur window size <= k
    L = 0

    for R in range(len(nums)):

        # Shifting L, remove
        # Since R-L + 1 = count of elements in window (calculating days we have same issue)
        # (difference is not the total no. of elements) plus one it for first element.
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1

        # If num already in window
        if nums[R] in window:
            return True

        window.add(nums[R])
    return False
