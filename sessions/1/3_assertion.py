# session 1
'''
The assert keyword is used when debugging code.
The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError.
You can write a message to be written if the code returns False, check the example below.
'''

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"


number = 42
assert number > 0 and isinstance(number, int), \
    f"number greater than 0 expected, got: {number}"


numbers = [1, 2, 3, 4, 5]
assert 4 in numbers