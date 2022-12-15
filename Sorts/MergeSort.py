#%%

# Divide and Conquer
# Break up the original arr to sub arr by spliting in halves. Till we get array of length 1, then compare?
## We we get individual eles/ arrays of length 1, we compare them and merge them back to a sorted array
# Naturally done by recursion


#%%


def merge(arr, startIdx, midIdx, endIdx):
    leftArr = arr[startIdx : midIdx + 1]
    rightArr = arr[midIdx + 1 : endIdx + 1]

    leftIdx = 0
    rightIdx = 0
    arrIdx = startIdx

    # Merge the two sorted halfs into a sorted array
    # Although the individual halfs are sorted, we need to compare the elements of the two halfs
    ## Efforts are reduced since we would only require to compare the 1st ele of each half, then move it to parent arr

    while leftIdx < len(leftArr) and rightIdx < len(rightArr):
        if leftArr[leftIdx] <= rightArr[rightIdx]:
            arr[arrIdx] = leftArr[leftIdx]
            leftIdx += 1
        else:
            arr[arrIdx] = rightArr[rightIdx]
            rightIdx += 1
        arrIdx += 1

    # One halfs may be odd number of elements
    ##  Remainder of the elements will be already sorted and, there is nothing to compare too. So just add them to the arr

    while leftIdx < len(leftArr):
        arr[arrIdx] = leftArr[leftIdx]
        leftIdx += 1
        arrIdx += 1

    while rightIdx < len(rightArr):
        arr[arrIdx] = rightArr[rightIdx]
        rightIdx += 1
        arrIdx += 1


def mergeSort(arr, startIdx, endIdx):
    if endIdx - startIdx == 0:
        return arr

    # Find the midIdx
    midIdx = (startIdx + endIdx) // 2

    # mergeSort recursively the left sub array
    mergeSort(arr, startIdx, midIdx)

    # mergeSort recursively the right sub array
    mergeSort(arr, midIdx + 1, endIdx)

    # merge the left and right sorted sub arrays

    # Compare and sort them, till we have elements in 1 half to compare too.
    # Once all the elements of 1 half is compared.
    # They other half can just be appended.

    merge(arr, startIdx, midIdx, endIdx)
    return arr


### Time Complexity

### Dividing the arrs to halfs
#
# Height of Binary Tree = logn

# How many times can we divide it?
# Till we get length of arrs = 1
# n / (2**k) = 1
# n =  2**k
# logn = k
# k = logn

# Time Complexity of Each Layer

# O(n) for merge, of Top layer  (Which includes n times comparisons)   ((# Insertion sort had O(n^2) comparisions))
# Even for bottom layer with 1 ele each, there would be n arrs to merge. So O(n)


# Total Time Complexity
# O(n) for Each layer
# logn layers
## O(nlogn) Time Complexity


### Space Complexity
# O(n), since we are creating new arrs for each layer (Recursion Stack)
