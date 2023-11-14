# Concepts

## Table Of Contents

### Outline

- :bulb: Think concept if:
- :writing_hand: Points for Coding it
- :star: Unique points

---

#### Greedy

A greedy algorithm is an intuitive problem-solving approach that makes the best possible decision at each step, hoping for a globally optimal solution.
It chooses locally optimal options without considering long-term consequences.

- The process involves initializing with an empty or given solution, making greedy choices based on specific criteria, checking feasibility, and continuing until a complete solution is found.

> The problem is divided into sub problems, choices are made and are propagated forward. (Thus optimizing solution)

- :bulb: Think Greedy if:
  - Propagting information
  - Incremental choices made

While it doesn't guarantee optimal solutions, it's efficient for some problems like finding the shortest path, activity selection, and Huffman coding. For more complex problems, other algorithms like dynamic programming or backtracking may be better for ensuring optimality.

Eg:

- [Kadane's Alg](https://github.com/senorbeast/dsa-py/blob/dev/Arrays/advAlgs/Kadanes.py) : maxSum of subarray is calcuated at every index, and propogated if needed for maxSum of subarray.
  - Choice it to propagate prevSum or use propagate 0, if prevSum is -ve.

- [Maximum SubArray (Kadane's Alg)](https://github.com/senorbeast/leetCode/tree/main/0053-maximum-subarray): Same as above

- [Jump Sum](https://github.com/senorbeast/leetCode/tree/main/0055-jump-game):      :star: Choice propogation starts from the end to beginning. The Goal is brought closer to the start.
  - :bulb: If choices can't be logically deducted. Start from the reverse direction.
  - Since any of route to victory doesn't matter.
  - (If we started propagation from the beginning we may not choose the victory path)

#### Sliding Window

- :bulb: Think Sliding window when
  - subarray (contiguos sub part of an array)
  - Need contiguos substring/subcollection from a bigger string/collection
- Types
  - Fixed: Rolling window, of fixed size
  - Variable:
    - Keeping R pointer incrementing,
    - Shrinking window from L side for a condn, with fixed R pointer.
    - May look O(n^2), but the L pointer overall only traverses the array ones. TC: O(2n) = O(n)
- :writing_hand: Condition, when subcollection is invalid
  - if invalid move left pointer (maybe once/many time)- right pointer is moved continuously usually
- :star: Using while inner loop instead of a if condn: It allows the left pointer to move many times, to get a smaller window. This will cover all the possible substrings (n^2 substrings). (Not required for all the problems)

#### Two pointers

- :bulb: Think Two pointers when
  - Want specific 2 elements.

- Wide use of two pointers, in other algs

#### preFixSum, postFixSum

- Precompute preFixSum/PostFixSum(SuffixSum)
  - Simple, preprocessing, reduced Time Complexity for further actions
  - TC: the prefix sum array is O(n),
  - TC: Each range sum query takes constant time O(1), making it an efficient solution for related problems.

#### Stacks

- First In, Last Out
- Last In , First Out
- :bulb: Think Stacks when
  - Last entry is required next
  - Something in the future decides, the state of prev problems, create a stack for left over problem. Resolve them, with the future values. Thus, requiring one iteration.
  - Keeping track of left over problems. (Sometimes)

  - :star: Left over problem approach
    - [Car Fleet](https://github.com/senorbeast/leetCode/blob/main/0853-car-fleet/0853-car-fleet.cpp), [Largest rectangle area histogram](https://github.com/senorbeast/leetCode/blob/main/0084-largest-rectangle-in-histogram/0084-largest-rectangle-in-histogram.cpp)

- Eg: Min Stack, Parentheses Problems,

#### Trees (Recursive)

- :bulb: Think Trees when
  - We have common part, then branching into choice
  - Recursiveness
  - Choices
  - To get everykind of permutation

- Complexities
- TC => Usually no. of nodes in the tree visited/created
- SC => Usually Max depth of recurse call * space used for each call

- x nodes => TC: O(x)
- height =>
  - b branches from each node
    - x = b^h => h =  log(x/b)

- Power Set
- Levels(height of tree) = n
  - If 2 nodes at each level
  - Total no. of nodes in tree = 2^n
    - If passing the n length output to next call, and saving output in each call not in place.
      - TC: O(n * 2^n)
      - SC: O(n * 2^n)
      - Auxillary TC: O(n)  (Space for nested n calls)

#### Backtracking (DFS++)

- :bulb: Think concept if:

- :writing_hand: Points for Coding it
  - Keep track of visited List (memoize visited nodes/vertex for 1 path)
  - :star: For more paths, remove current node from visited list,
  so its sibling in the stack call, (parent's another child in callstack)
  can go through the node.

  Basics:

  - Return 1 for succesfull path
  - Recursively DFS for each node, pass along visited list

- :star: Unique points


#### Graphs



#### Dynamic Programming

- 