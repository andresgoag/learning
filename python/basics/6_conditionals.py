# Truty and falsy values

bool(1) # True
bool(0) # False

# Conditional assigment
# and gives the first value if it is false, otherwise it gives you the second.
x = True and False
x is False
x = 35 and 0
x is 0
x = 0 and 35
x is 0

# or gives the first value if it is true, otherwise it gives you the second.
x = 0 or 35
x is 35
x = 35 or 0
x is 35

# not: denies the value
not True is False 




# Conditionals
# if: check a condition and execute a block if true
# elif: check another condition if the first one is false
# else: execute a block of code in case the other ones where false.

# To check if an object is instance of: isinstance(obj, type)



# Comparisons: ==, !=, >, <, >=, <=


def mean (value):
    if type(value) == dict:
        the_mean = sum(value.values())/len(value)
    else:
        the_mean = sum(value)/len(value)
    return the_mean

x = [1,2,3,4,5,6,7,8,9]
print(mean(x))

student_grades = {"Mary": 9.1, "sim":8.8, "John":10}
print(mean(student_grades))


x = 3
y = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x equals to y")
else:
    print("x is less than y")



x = 1
y = 1
if x == 1 and y==1:
    print("Yes")
else:
    print("No")


x = 1
y = 1
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
