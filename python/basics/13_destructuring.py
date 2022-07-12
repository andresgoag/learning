# assign more than one variable at a time on a single line.
x, y = 5, 11

# In fact, it's the commas which tell Python something is
# a tuple: we just add brackets for readability. In some instances 
# the brackets are actually necessary, in order to isolate the tuple 
# from the syntax around it, such as when we put a tuple inside a list.
x, y = (5, 11)

# We can also destructure a list or a set.
x,y = [1, 2]





# Destructuring in for loops
people = [
	("Bob", 42, "Mechanic"),
	("James", 24, "Artist"),
	("Harry", 32, "Lecturer")
]

for name, age, profession in people:
	print(f"Name: {name}, Age: {age}, Profession: {profession}")


# Enumerate function
example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
	print(counter, letter)

# 0 A
# 1 B
# 2 C




# Ignoring Values
person = ("Bob", 42, "Mechanic")
name, _, profession = person

print(name, profession)  # Bob Mechanic






# Using * to Collect Values

head, *tail = [1, 2, 3, 4, 5]

print(head)  # 1
print(tail)  # [2, 3, 4, 5]