## Rarely Used, Since there contraint in the range of elements (usually small ranges)
## Time Complexity: O(n)

## Alg

## Using idx as the element, value as the count.
## Using sorted nature of idx element.

# 1. Create a bucket for each element in the array
# Bucket Arr, store the number of occurance of each element, where idx represents the number in arr.

## That's why the range is limited for Bucket Sort, (To the range of max len of the array the lang provides)
## Since the max int can go from  2^63 - 1 [~9.2 billion] for 64 bit system, with int size as 4 bytes            
## 4 bytes for each element, For 8GB ram we are limited to 306 million elements in the array.

# 2. Increment count of each element in the bucket array (counts array)
# 3. Interate over the count array, and iterate over the number of counts of each element, to create the sorted arr.
# Since the index represents the element, and the value represents the number of occurance of that element. Iterating
# From the start, will give out sorted array.

#%%

# TC: O(n)
# SC: O(max(n)) 

def bucketSort(arr: list[int]) -> list[int]:

    # idx -> integer in arr
    # value -> count
    bucket: list[int] = [0] * (max(arr) + 1)   ## Idx represents the element, value is the occurence/count of that element.

    # O(n)
    for i in arr:
        bucket[i] += 1

    print(bucket)

    sortedArr = []

    # O(n),
    # Since len of bucket is range of ele (Take of x len)
    # And 2nd loop is count of each ele. (Take y len)
    # x + y = n, Since len of OG arr is n
    
    for i in range(len(bucket)): # Go over unique elements
        if bucket[i] != 0:
            for j in range(bucket[i]):   # Go over copies
                sortedArr.append(i)

    return sortedArr


#%%

arr = [1, 4, 1, 2, 7, 5, 2]
print(bucketSort(arr))

# %%

# Unstable Sort, we don't preserve order of ties

# We can create Stable Sort, by using LL for each count/bucket
