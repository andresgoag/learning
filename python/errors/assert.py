# assert allows you to check a condition, if the condition is false, 
# then the assertion raises an AssertionError.

word = 'bird'
assert len(word) > 0, "Word must not be blank"

# If the error is raised the message will be assigned to the error.




# if you want to split a long assertion line, then you can use \ for line 
# joining. The backslash at the end joins the assertion’s two physical lines 
# into a single logical line.
number = 42

assert number > 0 and isinstance(number, int), \
    f"number greater than 0 expected, got: {number}"