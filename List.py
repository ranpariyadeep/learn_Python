#List is mutable, means it can be changed or modified.

marks = [22, 45, 67, 89, 90]

print(marks)  # Output: [22, 45, 67, 89, 90]
print(marks[0])  # Output: 22
print(marks[1:3])  # Output: [45, 67]
print(marks[-1])  # Output: 90
print(marks[-3:])  # Output: [67, 89, 90]
print(marks[:2])  # Output: [22, 45]

len(marks)  # Output: 5

#multiple data types in a list
student = ["Deep", "Ranpariya", 22, 45.5, True]

list= [1, 2, 3, 4, 5]
list.append(6) # Adding an element to the end of the list
print(list)  # Output: [1, 2, 3, 4, 5, 6]

list.sort()  # Sorting the list in ascending order
print(list)  # Output: [1, 2, 3, 4, 5, 6]

list.sort(reverse=True)  # Sorting the list in descending order
print(list)  # Output: [6, 5, 4, 3, 2, 1]

list.reverse()  # Reversing the order of the list
print(list)  # Output: [1, 2, 3, 4, 5, 6]

list.insert(0, 0)  # Inserting an element at a specific index
print(list)  # Output: [0, 1, 2, 3, 4, 5, 6]
list.insert(1,3)
print(list) # Output: [0, 3, 1, 2, 3, 4, 5, 6]

list.remove(3)  # 1st '3' remove from list
print(list)  # Output: [0, 1, 2, 3, 4, 5, 6]

list.pop()  # Removing the last element from the list
print(list)  # Output: [0, 1, 2, 3, 4, 5]

list.pop(0)  # Removing the element at index 0
print(list)  # Output: [1, 2, 3, 4, 5]

list.clear()  # Clearing all elements from the list
print(list)  # Output: []

list2=list.copy()  # Creating a shallow copy of the list
print(list2)  # Output: []

