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
