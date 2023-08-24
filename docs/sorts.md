
#### Bucket Sort

- TC: O(n), SC: O(n)

- :writing_hand: Points for Coding it
  - Create Bucket Arr, store the number of occurance of each element. (Using idx as the element, value as the count)
  - Using sorted nature of idx element. Loop over bucket arr (count arr), and its count to create a new sorted arr. (Looks nested loops, but is O(n) (every element is covered once))

- Limitation:
  - Range is limited for Bucket Sort, (To the range of max len of the array the lang provides)
  - For cpp int, 64 bit system
    - Since the max int can go be in range 2^63 - 1 [~9.2 billion]
    - 4 bytes for each element, For 8GB ram we are limited to 306 million elements in the array

- Bucket Sort Variation:
  - Use whatever parameter you want to sort as index of array. Make sure that parameter is bounded.
  - The bounded range will be limited by the space available by the computer.
  - Eg. [Top K freq elements](https://github.com/senorbeast/leetCode/blob/main/0347-top-k-frequent-elements/0347-top-k-frequent-elements.cpp)

#### Insertion Sort

#### Merge Sort

#### Quick Sort
