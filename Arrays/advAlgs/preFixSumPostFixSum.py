#
## Prefix Sum
#
# [2,-1,3,-3,4]

# prefixs subarrays: [2], [2,-1], [2,-1,3]...

# preFixSum = [2,1,4,1,5]
# Keep adding prev sum to current element
# Total sum of array will be preFixSum[-1]

## Generally use to eliminate repeated work
## An array with n values, we have n^2 subarrays2
## Use prefix or postfix helps to make this efficient

# Precomputing work

#%%
from typing import List


arr =  [2,-1,3,-3,4]
#%% 

def preFixSum(arr: List[int]) -> List[int]:
    prevSum = 0
    for i in range(len(arr)):
        arr[i] += prevSum
        prevSum = arr[i]
    return arr

print(preFixSum(arr))

#%% 

def postFixSum(arr: List[int]) -> List[int]:
    postSum = 0
    for i in range(-1, -len(arr) -1, -1):
        arr[i] += postSum
        postSum = arr[i]
    return arr

print(postFixSum(arr))



# %%
# Given an array of values,
# design a data structure that can query the sum of a subarray of the values;

class PrefixSum:

    # TC: O(n) SC: O(n)
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
    
    # TC: O(1)
    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        # Using prev element of the left index
        preLeft = self.prefix[left -1] if left > 0 else 0
        return preRight - preLeft

arr =  [2,-1,3,-3,4]

prefixSumObj = PrefixSum(arr)
print(preFixSum(arr))
print(prefixSumObj.rangeSum(1,3))

# %%
