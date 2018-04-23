# sets

# The set data structure in Python models the mathematical definition of a set:
# an unordered collection of unique objects.
# The easiest way to think about sets is that they are like dictionaries without values; that is, the keys in a dictionary are a set.
# Checking whether something is in a set is very efficient compared to data structure like a list or tuple.
#
# Set literals are notated like dictionary literals, except that there are no values.
# To construct an empty set however, you need to use the set() function,
# ... as the {} literal is interpreted as an empty dictionary instead of an empty set.
numbers = set() # example how to create an empty set

duplicates = [1, 2, 1, 3, 1, 5, 2, 6, 7]
numbers = set(duplicates)
print(len(numbers), numbers)

# Because sets are unordered data structures, they cannot be indexed.

# Testing for membership (if x in y:) 
# and iterating over a set (for x in y:) 
# ... work in the same way as other data structures we have seen in Python.

# An object can be added to a set using the .add()
# Objects already in the set can be removed using the .remove() method
# Adding an object which is already in the set has no effect.
numbers = set([1,2,3])
numbers.add(5)
numbers.remove(2)
print(numbers)

# Mathematical sets have a number of standard operations that can be performed on two sets. Python sets have support for the union, intersection, and difference operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union
print(a & b)  # Intersection
print(a - b)  # Difference
print(b - a)  # Difference
print(a ^ b)  # Symmetric difference

# comparing sets
#   
#  Mathematical sets have three notions of comparison, which Python sets also implement. These are: is a subset, is a superset, and is disjoint.

a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2}
print(a.issubset(b), a.issuperset(b), a.isdisjoint(b))


# only hashable objects (it is mostly about being mutable) can be inserted into set (e.g. lists cannot)


