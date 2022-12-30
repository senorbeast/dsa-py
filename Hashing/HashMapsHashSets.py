## Applications

## Hash Maps and Hash Sets

# Sets are array like
# Maps are key value pair (dictionary like)

## Maps
# Key is used to sort the BST
# Also used to access values from ## HashMaps

## TreeMap or BST vs HashMap
# Image

## HashMap
# Insertion/Deletion is AVG O(1),
# Although Big-O means worst cases, its real worst case is O(n)
# But we usually take it to be ## O(1)
## TC: O(1), for Insertion and Deletion

## HashMap are not allowed duplicates, just as a BST.

# Creating a HashMap, takes ## TC: O(n),     SC: O(n)
# Creating a TreeMap, takes ## TC: O(nlogn), SC: O(n)

#%%
names = [
    "Ganguly",
    "Kohli",
    "Tendulkar",
    "Mbappe",
    "Messi",
    "Pele",
    "Chettri",
    "Tendulkar",
]

# Python Dictionaries are HashMaps
countMap = {}

for name in names:
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1

print(countMap)

# %%
