### List

- we know all bla bla on list for now...
- let's look at example of sorting methonds `.sort()` vs `sorted(lst)`

- `.sort()` : this is inplace shorting , it sorts the list in place, it means that it sorts the list that you are calling the method on , it does not return a new list, it sorts the list that you are calling the method on.

- `sorted(lst)` : this is not inplace sorting, it returns a new sorted list, it does not sort the list that you are calling the method on, it returns a new list that is sorted.

> NOTE (!): List slicing won't give you errors. what i want to say let's check. 
```py
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst[1:3])  # [2, 3] this is fine
# But what if... 
sliced1 = lst[20:25] # if you give this lind of indexes then this will give you an empty list
sliced2 = lst[-10: -15]

```

> Q: what was the design idea of slice functionlity in py? something like why it does not give you an error when you give it invalid indexes? this behaviour and why this kind what is the thinking behind it?

- when we are making copy of the list the both object refers the same list in memory which means if you change in copy of org list then i will reflect same in org list.
- To prevent this behaviour we use `.copy()` method  or `list()` function to make a copy of the list.

### Tuple
- Tuples are immutable, you can't change the value of a tuple after it's created.

```py

# what is you want to make a tuple have single element?
t = (1) # this is not a tuple, this is an integer or string if you put value like ("hey")
# so for that you need to do...
t = (1,) # this is a tuple. adding "," (comma) at the end is what makes it a tuple.
```

- wokring with tuples is faster than working with lists.


### Dictionary
- Dictionaries are mutable, you can change the value of a dictionary after it's created.
- Dictionaries are unordered, you can't rely on the order of the items in a dictionary.
- When you wan to copy a dict it has same behaviour which list has. you need to use `.copy()` method or `dict()` function to make a copy of the dict

### Set
- Sets are unordered, you can't rely on the order of the items in a set.
- Sets are mutable, you can change the value of a set after it's created.
- Sets are used to store unique values, you can't have duplicate values in a set.
- use `.discard()` to remove a element from a set.
- set has `union()` `intersection()` `difference()` `symmetric_difference()` methods.
- same as dict you need to use `.copy()` method or `set()` function to make a copy of the set.
- **frozenset()** is immutable set.