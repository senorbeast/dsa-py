# Concepts

## Table Of Contents

### Outline

- :bulb: Think concept if:
- :writing_hand: Points for Coding it
- :star: Unique points

---

#### Greedy

A greedy algorithm is an intuitive problem-solving approach that makes the best possible decision at each step, hoping for a globally optimal solution.
It makes locally optimal choices at each step without considering their long-term impact.

- The process involves initializing with an empty or given solution, making greedy choices based on specific criteria, checking feasibility, and continuing until a complete solution is found.

> The problem is divided into subproblems, and choices are made based on these subproblems. These choices are then propagated forward in the algorithm. (Thus optimizing the solution)

- :bulb: Think Greedy if:
  - Propagating information
  - Incremental choices made

While it doesn't guarantee optimal solutions, it's efficient for some problems like finding the shortest path, activity selection, and Huffman coding. For more complex problems, other algorithms like dynamic programming or backtracking may be better for ensuring optimality.

- :star: Unique points
  - Intuitive Decision-Making

Eg:

- [Kadane's Alg](https://github.com/senorbeast/dsa-py/blob/dev/Arrays/advAlgs/Kadanes.py) : Calculate the maximum sum of a subarray at every index and propagate it if needed for the maximum sum of the subarray.
  - Choose to propagate the previous sum or propagate 0 if the previous sum is negative.

- [Maximum SubArray (Kadane's Alg)](https://github.com/senorbeast/leetCode/tree/main/0053-maximum-subarray): Same as above

- [Jump Sum](https://github.com/senorbeast/leetCode/tree/main/0055-jump-game): :star: Choice propagation starts from the end to the beginning. The goal is brought closer to the start.
  - :bulb: If choices can't be logically deduced, start from the reverse direction.
  - Since any route to victory doesn't matter.
  - (If we started propagation from the beginning, we might not choose the victory path)

#### Sliding Window

- :bulb: Think Sliding window when
  - Dealing with a subarray (a contiguous subpart of an array)
  - Needing a contiguous substring/subcollection from a larger string/collection
- Types
  - Fixed: Rolling window of a fixed size
  - Variable:
    - Incrementing the R pointer,
    - Shrinking the window from the L side based on a condition, with the R pointer fixed.
    - Although it might seem O(n^2), the L pointer traverses the array only once. TC: O(2n) = O(n)
- :writing_hand: Condition, when the subcollection is invalid
  - If invalid, move the left pointer (maybe once/many times); the right pointer is usually moved continuously.
- :star: Using a while inner loop instead of an if condition: It allows the left pointer to move multiple times to obtain a smaller window. This covers all possible substrings (n^2 substrings). (Not required for all problems)

- :star: Subarray Focus: advantageous for problems involving contiguous subarrays. 
It efficiently narrows down the search space and often leads to linear or linear-logarithmic time complexity solutions.

#### Two Pointers

- :bulb: Think Two pointers when
  - You need to consider specific 2 elements.

- Two pointers are widely used in other algorithms.
- :star: Unique
  - Focus on Pairwise Interaction: The Two Pointers Approach shines when you need to consider and interact with specific pairs of elements.

#### PreFix Sum, PostFix Sum

- Precompute preFixSum/PostFixSum (SuffixSum)
  - Simple preprocessing that reduces Time Complexity for further actions
  - TC: The prefix sum array is O(n)
  - TC: Each range sum query takes constant time O(1), making it an efficient solution for related problems.

- :bulb: Think Prefix/ PostFix Sum when
  - calculating the sum of elements within a specific range.
  - frequent range sum calculations.

- :star: Unique
  - Constant-Time Range Sum Queries: Pre computer commulative sum

#### Stacks

- First In, Last Out
- Last In, First Out
- :bulb: Think Stacks when
  - The last entry is required next
  - Something in the future determines the state of previous problems; create a stack for leftover problems. Resolve them with future values, requiring one iteration.
  - Keeping track of leftover problems (Sometimes)
  - keep track of the most recent entries or perform operations in reverse order of insertion.
  - :star: Leftover problem approach
    - [Car Fleet](https://github.com/senorbeast/leetCode/blob/main/0853-car-fleet/0853-car-fleet.cpp), [Largest rectangle area histogram](https://github.com/senorbeast/leetCode/blob/main/0084-largest-rectangle-in-histogram/0084-largest-rectangle-in-histogram.cpp)


- Eg: Min Stack, Parentheses Problems

#### Trees (+ Recursion Decision Tree)

- :bulb: Think Trees when
  - There's a common pattern that branches into choices
  - Recursiveness is involved
  - Choices need to be made
  - All permutations are required

- Complexities
- TC => Usually the number of nodes in the tree visited/created
- SC => Usually the maximum depth of recursive calls * space used for each call

- :star: Unique
  - Can be traversed in 4 ways: Inorder, ReversedOrder, preOrder, postOrder
  - Structured Problem Solving:  when there's a clear hierarchical relationship between choices or subproblems

- x nodes => TC: O(x)
- height =>
  - b branches from each node
    - x = b^h => h =  log(x/b)

- Power Set
- Levels (height of tree) = n
  - If 2 nodes at each level
  - Total number of nodes in the tree = 2^n
    - If passing the n-length output to the next call and saving output in each call not in place.
      - TC: O(n * 2^n)
      - SC: O(n * 2^n)
      - Auxiliary TC: O(n) (Space for nested n calls)

#### Backtracking (DFS++)

- :bulb: Think Backtracking when:
  - You need to explore all possible paths to find a solution.

- :writing_hand: Points for Coding it
  - Keep track of a visited List (memoize visited nodes/vertices for one path)
  - :star: For more paths, remove the current node from the visited list. This allows its sibling in the stack call (another child of the parent) to be traversed. ( :star: backtracking involves undoing choices and exploring further.)

  Basics:
  - Return 1 for a successful path
  - Recursively perform DFS for each node, passing along the visited list

- :star: Unique points
  - Exploring All Paths: It's ideal for combinatorial problems where all combinations need to be evaluated.

#### Dynamic Programming

- Optimizing recursive functions

##### Top-Down DP (Memoization)

- Breaking the Problem into Sub-problem, solving the sub problem
- :star: Problem, subproblem can be usually be related in form of Equation in DP

- Memoization (Caching) (Optimizing recursion) (Top-Down DP)
  - Think Fibonacci 5 -> reqs f(4), f(3) -> reqs ...
  - :writing_hand: Points for Coding it
    - Write the recursive brute force approach
    - Cache result.
    - Use cache if available, as addn base condn.
  - :bulb: Think Memoization DP when:
    - Parts of recursive decision tree are repeated
    - :star: Optimizing TC of recursive function by caching.
  - Usless, when all decision nodes of tree are unique.

##### Bottom Up DP (True DP)

- Understand the recursive way for it.
- Mathematically calculate, by referencing the recursive returns.
- May use maths tricks, more base condns. (More defined boundaries, to make the pattern of calc easier)
- Loop in reverse order, (BOTTOM-UP)

- Bottom-Up DP (called True DP by some)
  - Think Bottom-up Fibonacci 0 + 1 = 2, 1 + 2 = 3....
  - :bulb: Think Bottom-Up DP when:
    - :star: Optimize SC of memoizedRecursiveFunction.
- :writing_hand: Points for Coding it
  - Go over recursive approach, think over, from bottom up of the recursive decsion tree
  - How one entity is related to other mathematically
  - Creating more boundaries (base condn like), can help ease the maths
  - Look for pattern, how one entity depends on its next.

- Eg: Counting paths with DP
  - Here 2 pieces of information were used for each iteration
  - prevRow (empty initially), last element of each row be will 1
  - These were used to calc the no. of paths available at each node. (We got to know we should do this because we thought recursively first)
    - currRow[c] = currRow[c+1] + prevRow[c], our equation for each element of the currRow.
