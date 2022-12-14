# Sorting can be used for arrays or LLs

# Break the problem to sub probs
# Eg. [2,3,4,1,6]

# Sort first 1 ele, then first 2 eles and so on.
## Since we are solving it by sub problems, we can use recursion

# We will be using an interative approach


arr = [2, 3, 4, 1, 6]

## Assume 1 ele as [2] an sorted sub array
## We have a sorted sub array and an unsorted sub array
## We will pick the first element of the unsorted sub array and insert it into the sorted sub array
## Do Swaps
## i -> Pointer for fresh variable in unsorted array
## j -> Pointer in sorted sub array, will be used for comparision with ith ele
## j will help us to insert (swap, swap...) the ith ele in the correct position in the sorted sub array

# %%
def insertionSort(arr):
    for i in range(1, len(arr)):
        # Pointer in sorted sub array, will be used for comparision with ith ele
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
            j -= 1  # move pointer to left, for comparision with smaller ele
            # j + 1 will be the new ele to be inserted in the sorted sub array always
    return arr


#%%
arr = [3, 4, 2, 5, 1, 6]
print(insertionSort(arr))

# %%

# We can sort any values if they are comparable.
# Eg. string, chars, objects, time, dates, age ....


# Stable vs Unstable Sorting

# 7',3,7
#
# Stable -> 3,7',7
# Unstable -> 3,7,7'

# Both are right, Stable preserves the tie.
# Unstable may or may not preserve the tie.

## Time Complexity

## Insertion sort on a sorted list: O(n - 1) = O(n)
# Just comparing if first element of unsorted sub array is
# greater than the last element of sorted sub array
# And thats always true for a sorted list
## Inner while loop will run never run for a sorted list

## Insertion sort on a reverse sorted list:
# Loop through the array, compare neighbour i-1 times
## Inner while loop will run i-1 times for a reverse sorted list

# No. of Operations
# 1 + 2 + 3 + ... + (n-1) = n(n-1)/2 = O(n^2 - n)/2 = O(n^2)

# Max case would be O(n^2)
# Last element of unsorted arr will  be compared with all eles of sortted arr (n-1) comparision.
# Looped over for n arr length. O(n^2)


# Best Case O(n)
# Worst Case O(n^2)
