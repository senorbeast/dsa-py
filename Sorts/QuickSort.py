# Instead of spliting the arr and then sorting the halfs

# We select a random ele, for convience the right most value,
## We call it pivot value.
# Then we iterate through the rest of arr, and compare it with the pivot value.
# Values less than pivot go the a leftArr, greater than pivot go the RightArr
# Paritioning won't take extra Memory. We can do it in the same arr.


# Keeping track with 2 pointers
# (leftIdx) for swapping values less than the pivot, to the start
# (i) for iterating through the restOfArr

# startIdx, endIdx : To keep track of sub problems for recursion

## Time Complexity
## Worst: O(n^2)
## Avg: O(nlogn)


## Space Complexity
# No additonal space required

# If pivot is not a mean value, height of tree would can reach n
# And n comparisions in each layer would take, Time Complexity for worst case to be O(n^2)

# Picking the pivot cleverly, on average we can divide the array in almost equal halfs
# That would reduce the height of tree to logn, similar to merge sort.(which had splitting at mid point)
# Each layer comparision would take <n operations
# So on avg Time Complexity can be O(nlogn)


# Although all operations are done in same arr, we can imagine it as splitting the arr into sub arrs.. so on into a tree.

#%%
# QuickSort is unique
# Comparing with the pivot, divide and recurse
# Stop when divded sub array len = 1


def quickSort(arr: list[int], startIdx: int, endIdx: int) -> list[int]:

    # Base Case, when len(arr) = 1 (Sorted sub array)
    # ! Cannot use endIdx - startIdx = 0, to indicate len(arr) = 1
    # Since the idx are given by leftIdx - 1 or leftIdx + 1,
    # Pointed arr lengths can go 0 or 1, may not always come out to 1
    # TODO: We can think on it tho

    if endIdx - startIdx + 1 <= 1:  # Length of arr = 1
        return arr

    # Selecting the pivot value
    pivot = arr[endIdx]

    # LeftIdx: For swapping values less than pivot
    leftIdx = startIdx

    # Paritioning: Elements smaller than pivot will swap with (leftIdx) swapIdx.
    # Elements smaller than pivot will be swapped to the left, greater than pivot will be automatically swapped to the right.

    # Iterating through the rest of arr (not including pivot)
    for i in range(startIdx, endIdx):
        if arr[i] < pivot:
            arr[leftIdx], arr[i] = arr[i], arr[leftIdx]  # Swap ith ele with leftIdx
            leftIdx += 1

    # Swap the pivot with the leftIdx
    # Since thats where pivot will naturally be placed.
    # Left side of it will have smaller value than pivot, right will have greater values
    arr[leftIdx], arr[endIdx] = arr[endIdx], arr[leftIdx]  # arr[endIdx] is the pivot

    # Quick sort on left sub arr, right arr
    # leftIdx - 1, since leftIdx is the pivot now, Which has found it right place.
    # arr[leftIdx - 1] would the new pivot for the sub arr

    quickSort(arr, startIdx, leftIdx - 1)
    quickSort(arr, leftIdx + 1, endIdx)

    # All the operations happen, in same arr. Mutating the arr, so no new extra space required.
    # No need to merge the arr or anything, since the Pivot in each recursive step finds it right place.

    return arr


#%%

arr = [5, 2, 15, 4, 5, 1, 4, 7]
arr2 = [3, 4, 2, 5, 1, 6]
print(quickSort(arr, 0, len(arr) - 1))
print(quickSort(arr2, 0, len(arr2) - 1))

# %%

# Stable
# May not preserve the relative order during tie, due to swaps.

## Quick Sort is Unstable sorting alg.
