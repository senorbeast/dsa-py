## Rarely Used, Since there contraint in the range of elements (usually small ranges)
## Time Complexity: O(n)

## Alg

# 1. Create a bucket for each element in the array
# Bucket Arr, store the number of occurance of each element, and store it at that index.
## That's why the range is limited for Bucket Sort, (To the range of max len of the array the lang provides)
# 2. Increment count of each element in the bucket array (counts array)
# 3. Interate over the count array, and iterate over the number of counts of each element, to create the sorted arr.
# Since the index represents the element, and the value represents the number of occurance of that element. Iterating
# From the start, will give out sorted array.

#%%


def bucketSort(arr: list[int]) -> list[int]:
    bucket = [0] * (max(arr) + 1)

    # O(n)
    for i in arr:
        bucket[i] += 1

    print(bucket)

    sortedArr = []

    # O(n),
    # Since len of bucket is range of ele (Take of x len)
    # And 2nd loop is count of each ele. (Take y len)
    # x + y = n, Since len of OG arr is n

    for i in range(len(bucket)):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                sortedArr.append(i)

    return sortedArr


#%%

arr = [1, 4, 1, 2, 7, 5, 2]
print(bucketSort(arr))

# %%

# Unstable Sort, we don't preserve order of ties

# We can create Stable Sort, by using LL for each count/bucket
