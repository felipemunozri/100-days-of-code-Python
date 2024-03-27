# List comprehension is when we create a list from another list. It's not exclusive for lists, it can be used with
# tuples, ranges, or other iterables. The basic syntax of a list comprehension is new_list = [new_item for item in list]

# Without list comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# With list comprehension, new_list = [new_item for item in list]
new_list2 = [n + 1 for n in numbers]
print(new_list2)

# If we use conditionals then the syntax would be something like new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


uppercase_names = [name.upper() for name in names if len(name) > 5]

