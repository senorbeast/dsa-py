#### Tricks

##### Looks like O(n^2), but is O(n)

- Nested loops, but the inner loop runs conditionally. Rendering the total operations proportional to n
  - Eg. BucketSort, LongestSequenceLength,

##### Memoization


### Insights

> In context with dsa-py, LeetCode questions (in cpp, py)

#### Linked List

- Preferably create LL with empty head and tail Nodes. (Node with val = 0). It will be easier to handle removing and adding nodes.
  Usefull in LRU Cache

#### Hashmaps

- Relationships in between a collections of entities, can be transfer to another collections of entities. With HashMaps.
  - Use 1 collections as keys, other as values.
    Go over the hashmap, and copy the relationship.
    (Relation should be encoded in the elements/entities itself).

#### Recursion

- Merge Sort and Quick Sort, both use recursion, but one uses postorder, the latter uses preorder.

#### Out of the box

- Using constraint information.
  - Eg: Q.141 - // Stopping iteration with the constraint value. To solve in constant memory.

#### Question to revise

- [LRU cache](https://github.com/senorbeast/leetCode/tree/main/0146-lru-cache) (hashmaps to search nodes in O(1), LL to store recency order)
  - TC: O(1), SC: O(capacity)
  - both put and get functions affect recency order.
  - dealloacte memory in cpp

- [Sliding Window variable](https://github.com/senorbeast/dsa-py/blob/dev/Arrays/advAlgs/slidingWindowVariable.py)
  - :star: Shortest Subarray problem
  - Seems to be O(n^2), but overall is O(n)

#### Good cpp

- shared meomry pointer
- unique pointers
- dont play around with pointers

### For Interviews

#### SDE 1

- DSA
- LLD
- Machine Coding

#### SDE 2

- HLD

#### Managerial

- STAR
