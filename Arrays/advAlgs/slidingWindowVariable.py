# Find the length of the longest subarray, with the same value in each position


# %%
arr = [4, 2, 2, 3, 3, 3]

# res: Keep track of length of longest window.

# To keep the window valid,
# Once we get valid window update res, increment right pointer.


# TC: O(n)


def longestSubarray(nums) -> int:
    length = 0
    L: int = 0

    for R in range(len(nums)):
        # Update window when new R found.
        # Update L only if new subarray, if found.
        # i.e nums[R] is a new value compared to nums[L]
        if nums[L] != nums[R]:
            L = R

        # if in same window, update length in each iteration
        length = max(length, R - L + 1)

    return length


print(longestSubarray(arr))

# %%

# Find the minimum length subarray, where the sum if greater
# than or equal to the target. Assume all values are positive.


arr2 = [2, 3, 1, 2, 4, 3]

# Once we get 1 subarray, with sum >= target, extending the window
# will increase the sum, but also the length
# So, no need to extend the window. After 1 Match


# TC: O(n):
# The inner loop sometimes runs, sometimes once or more.
##  But the in total, the inner runs n times.
# # And not n*n as for usual inner loops. with O(n^2) TC.
# So, here total TC is O(2n) = O(n)


def shortestSubarray(nums, target) -> float:
    L, total = 0, 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]  # Add nums till we reach target

        # Keeping shrinking window if total sum is >= target
        # Shrink from the left side, keep the right pointer at the same pos
        while total >= target:  
            length = min(R - L + 1, length)  # Update res
            # For min length match, check with incre L
            total -= nums[L]
            L += 1

    return 0 if length == float("inf") else length


print(shortestSubarray(arr2, 6))

# %%
