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

-

#### Out of the box

- Using constraint information.
  - Eg: Q.141 - // Stopping iteration with the constraint value. To solve in constant memory. 



#### Question to revise

- LRU cache (hashmaps to search nodes in O(1), LL to store recency order) 
  - TC: O(1), SC: O(capacity) 
  - both put and get functions affect recency order.
  - dealloacte memory in cpp