# Dictionary used to store key-value pairs

# key can be of any immutable type (string, number, tuple)
#but key can not be of mutable type (list, set, dict)
# value can be of any type (mutable or immutable)
# can not duplicate keys, but can have duplicate values.
# Dictionary is mutable, meaning it can be changed or modified.

# Dictionary is unordered, meaning the items do not have a defined order.
# Dictionary is indexed by keys, not by position.


dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "Pass_Subjects": ("Math", "Science"),
    "grades": {
        "Math": 90,
        "Science": 85,
        "History": 88
    }
}

null_dict = {}  # Empty dictionary
null_dict["name"] = "Deep Ranpariya"  # Adding a key-value pair

print(dict)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York', 'is_student': False, 'courses': ['Math', 'Science', 'History'], 'grades': {'Math': 90, 'Science': 85, 'History': 88}}
print(dict["name"])  # Output: John Doe
print(dict["age"])  # Output: 30
print(dict["courses"])  # Output: ['Math', 'Science', 'History']
print(dict["grades"]["Math"])  # Output: 90


# Accessing  key 
print(dict.keys())  # Output: dict_keys(['name', 'age', 'city', 'is_student', 'courses', 'Pass_Subjects', 'grades'])

#type casting

print(list(dict.keys()))  # Output: ['name', 'age', 'city', 'is_student', 'courses', 'Pass_Subjects', 'grades']
print(dict) 

#length of dictionary
print(len(dict))  # Output: 7, number of key-value pairs in the dictionary
print(len(dict["grades"])) # Output: 3, number of key-value pairs in the nested dictionary 'grades'

#values
print(dict.values())  # Output: dict_values(['John Doe', 30, 'New York', False, ['Math', 'Science', 'History'], ('Math', 'Science'), {'Math': 90, 'Science': 85, 'History': 88}])

#items - it returns a view object that displays a list of a dictionary's key-value tuple pairs
print(dict.items())  # Output: dict_items([('name', 'John Doe'), ('age', 30), ('city', 'New York'), ('is_student', False), ('courses', ['Math', 'Science', 'History']), ('Pass_Subjects', ('Math', 'Science')), ('grades', {'Math': 90, 'Science': 85, 'History': 88})])

#get - it returns the value for the specified key if key is in dictionary, else default value
print(dict.get("name"))  # Output: John Doe
print(dict.get("country", "USA"))  # Output: USA (default value if key not found)

#update - it updates the dictionary with the specified key-value pairs
dict.update({"country": "USA", "is_student": True})
 # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York', 'is_student': True, 'courses': ['Math', 'Science', 'History'], 'Pass_Subjects': ('Math', 'Science'), 'grades': {'Math': 90, 'Science': 85, 'History': 88}, 'country': 'USA'}

#pop - it removes the specified key and returns the value
removed_value = dict.pop("age")
print(removed_value)  # Output: 30
 # Output: {'name': 'John Doe', 'city': 'New York', 'is_student': True, 'courses': ['Math', 'Science', 'History'], 'Pass_Subjects': ('Math', 'Science'), 'grades': {'Math': 90, 'Science': 85, 'History': 88}, 'country': 'USA'}