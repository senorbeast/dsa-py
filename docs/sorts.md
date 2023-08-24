# Sorts

## Table Of Contents

### Outline

- :bulb: Think concept if:
- :writing_hand: Points for Coding it
- :star: Unique points

#### Bucket Sort (As index sort)

- TC: O(n), SC: O(n)

- :writing_hand: Points for Coding it
  - Create Bucket Arr, store the number of occurance of each element. (Using idx as the element, value as the count)
  - Using sorted nature of idx element. Loop over bucket arr (count arr), and its count to create a new sorted arr. (Looks nested loops, but is O(n) (every element is covered once))

- Limitation:
  - Range is limited for Bucket Sort, (To the range of max len of the array the lang provides)
  - For cpp int, 64 bit system
    - Since the max int can go be in range 2^63 - 1 [~9.2 billion]
    - 4 bytes for each element, For 8GB ram we are limited to 306 million elements in the array

  - Unstable Sort

- :star: Unique Points:
  - Efficiency for Bounded Ranges: highly efficient when dealing with elements within a bounded range.
- Bucket Sort Variation:
  - Use whatever parameter you want to sort as index of array. Make sure that parameter is bounded.
  - The bounded range will be limited by the space available by the computer.
  - Eg. [Top K freq elements](https://github.com/senorbeast/leetCode/blob/main/0347-top-k-frequent-elements/0347-top-k-frequent-elements.cpp)

#### Insertion Sort (Swapper Swapper)

- TC: O(n^2)
- SC: O(1)  Although in place sorting
- :writing_hand: Points for Coding it
  - Two pointers
  - Let 1st element be the "sorted arr"
  - Iterate over the unsorted arr
    - Take j = i - 1
    - Compare j and j + 1, swap them if jth ele is bigger
    - Keep swapping till jth is bigger.
- :star: Unique points
  - No extra space required.
  - Best for Small Lists: efficiently handle small lists make it or already partially sorted
  - Stable

#### Merge Sort (Divide and Conquer) (Postorder recursion)

- Sort smallest subproblem, merge and keep sorting (easier since it's subproblem is sorted, need to compare 1st element and insert)

- TC: O(nlogn)  SC: O(n) Creating copies while merging.
- :writing_hand: Points for Coding it
  - Divide and Conquer
  - Recursively spilt array with midval, till arr length is 1
  - Then merge them in sorted manner, by 2 pointers, starting comparision from the left to right.
  - All this can be done with pointers, no need to create new var.
  
- :star: Unique points
  - Although conceptually its recursive and looks like a tree.
  - Recursion is managed by pointers and reference to the same array. (No extra space needed)
  - Stable

#### Quick Sort (Divide and Conquer) (Preorder recursion)

- Sort big units somewhat, split into subproblems and sort. (easier since only half is left to sort now, compared to prev step)

- TC: O(n log n) (average case), O(n^2) (worst case)
- SC: O(log n) (average case), O(n) (worst case)

- :writing_hand: Points for Coding it
  - Choose a pivot element from the array (often the last element).
  - Partition the array into two subarrays: elements less than the pivot and elements greater than the pivot.
  - Recursively apply Quick Sort to the subarrays.
  - Combine the sorted subarrays to obtain the final sorted array.

- :star: Unique points
  - Efficient sorting algorithm for large datasets.
  - In-place sorting, requires minimal additional memory.
  - Divide-and-conquer strategy: breaks down the sorting problem into smaller subproblems.

- Limitation:
  - Worst-case time complexity can degrade to O(n^2) if the pivot choice is consistently poor (e.g., choosing the smallest or largest element as pivot).

- Quick Sort Variation:
  - Randomized Quick Sort: Instead of always choosing the last element as the pivot, select a random element as the pivot to improve average-case performance.
