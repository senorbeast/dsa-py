# %%

## Two pointers
# Sliding window is subset of Two pointers

# But in two pointers, we usually care about the elements
# pointed by 2 pointer,

# But in sliding window we care about all the elements in between too.


# %%

# Check if an array is a palindrome


# Two pointers on the edges, come closer while
# Doesn't check the middle value (Dont care about it for palindrome)
# checking for equality
# TC: O(n)
# SC: O(1)
def palindrome(word) -> bool:
    L, R = 0, len(word) - 1

    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1

    return True

words = ["malayalam", "woow", "wow","b","","Goodbye"]
for word in words:
    print(word,": ",palindrome(word))



# %%

# Given a sorted input array, return the two indices of two
# elements which sum up to the target value.
# Assume there's exactly one solution.


# TC: O(n)
# SC: O(1)
def twoSumSorted(nums, target) -> list[int]:
    L, R = 0, len(nums) - 1

    while L < R:
        twoSum = nums[L] + nums[R]

        if twoSum > target:
            R -= 1
        elif twoSum < target:
            L += 1
        else:
            return [L, R]

    return []  # Will never return this. Since there's exactly one sol.
