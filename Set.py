#Set is a collection of unique elements.
# set is mutable, meaning it can be changed or modified.,
#But it elements can not be changed, but can be added or removed.
# Sets are unordered, so the items do not have a defined order.
#list and dict can not be used as keys in a set. - bsc it's mutable.
# Sets are indexed by position, but the order is not guaranteed.

nums = {1, 2, 3, 4, 5}  # Set of numbers
print(nums)  # Output: {1, 2, 3, 4, 5}

nums2 = {1,2,2,3,4,5}  # Set of numbers with duplicate
print(nums2)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)

collection = {"apple",1,3, "banana",1,2,3, "cherry","banana"}  # Set of `mixed types
print(collection)  # Output: {1, 2, 3, 'apple', 'banana', 'cherry'} (duplicates are removed)`


#add & remove elements
empty_set = set()  # Empty set
empty_set.add("Deep Ranpariya")
print(empty_set)  # Output: {'Deep Ranpariya'}
empty_set.remove("Deep Ranpariya")  # Removing an element
print(empty_set)  # Output: set() (empty set)


empty_set.add("Deep")
empty_set.add("Ranpariya")  # Adding another element
print(empty_set)  # Output: {'Deep', 'Ranpariya'}

empty_set.clear()  # Clearing the set
print(empty_set)  # Output: set() (empty set)


k=nums.pop()  # Removing and returning an arbitrary element (not recommended for empty sets)
print(k)  # Output: 1 (or any other element, as sets are unordered)
o=nums.pop()
print(o)  # Output: 2 (or any other element, as sets are unordered)


#Union & Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # Union of two sets
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1.intersection(set2)  # Intersection of two sets
print(intersection_set)  # Output: {3} (common elements)

