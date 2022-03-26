"""
This file contain basics of SET:
    -Sets are used to store multiple items in a single variable.
    -Set is one of 4 built-in data types in Python used to store collections of data.
    -A set is a collection which is unordered, unchangeable*, and unindexed.
    -Sets are written with curly brackets.
NB: Set items are unchangeable, but you can remove items and add new items.

"""
set01 = {"fitsum","misrak","solomon","dawit"}
print(set01)

"""Note: Sets are unordered, so you cannot be sure in which order the items will appear."""
"""Set items are unordered, unchangeable, and do not allow duplicate values.
Unordered:
    -Unordered means that the items in a set do not have a defined order.
    -Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
Unchangeable:
    -Set items are unchangeable, meaning that we cannot change the items after the set has been created.
    -Once a set is created, you cannot change its items, but you can remove items and add new items.
"""

#Get the length of the set
print("The size of the set: ",len(set01))

#Get the datatype
print("The data types of the set will be displayed like: ",type(set01))

"""
The set() Constructor
It is also possible to use the set() constructor to make a set. we have to use double rounded bracket in the set
"""
print("\n\n\n")
set02 = set(("selemon","misrak","dawit","fitsum"))
print(set02)

"""
Python Collections (Arrays):
    
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable.
Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. 
Allows duplicate members.

Set is a collection which is unordered, unchangeable*, and unindexed. 
No duplicate members.

Dictionary is a collection which is ordered** and changeable.
No duplicate members.


Access Items
You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

set03 = set(("selemon","misrak","dawit","fitsum"))
for x in set03:
    print(x)

print("\n\n\n")
"""
Change Items
Once a set is created, you cannot change its items, 
but you can add new items.


1. To add one item to a set use the add() method.
"""
set04 = {1,2,3,4}
print(set04)
set04.add(5)
print(set04)

"""
Add Sets:
To add items from another set into the current set, 
use the update() method.
"""
print("\n\n\n")
set05 = {1,2,3,4}
print(set05)

set06 = {6,7,8,9}
set05.update(set06)
print(set05)

"""
Add Any Iterable
The object in the update() method does not have to be a set, 
it can be any iterable object (tuples, lists, dictionaries etc.).
"""