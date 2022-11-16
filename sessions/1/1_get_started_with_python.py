# session of 1
'''
# HELLO WORLD!! #
What is Python?
It is used for:
web development (server-side),
software development,
mathematics,
system scripting.

What can Python do?
Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.

Why Python?
Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.

Reference:
https://www.w3schools.com/python/python_intro.asp
'''

print("Hello, World!")

# 1) CommandLine
'''It is quickest and easiest sometimes not to write a code file. So Python can be run as a command line itself.
to quit the command line interface just ctrl + c or exit()'''

# 2) Syntax
if 5 > 2:
  print("Five is greater than two!")
  if 2 < 5:
    print("Two is less than five!")

x = 5
y = 'My Name is \n'
z = ['What?', 'Who?']
print(y*x)


# 3) Comments
# This is a comment
''' This is also a comment but I will be Multi Line comments without adding # in each line'''

# 4) Be careful
# Getting the data type
print(type(x))
# Case-sensitive
a = 'I am a'
A = 'I am A, not a'

# 5) Naming convention
# Google Python Style Guide is our reference
'''module_name, package_name, ClassName, method_name, ExceptionName, 
function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, 
function_parameter_name, local_var_name.
A similar naming scheme should be applied to a CLASS_CONSTANT_NAME'''


# if a variable is a constant, it's uppercase as shown below:
FIRST_NAME = 'Jon'
# This means Jon is not planning to change his name in this life.

# functions
name = 'Jon'
# if they're more than one word, they're separated with underscore "_" as shown below:
def add_last_name(first_name, last_name):
    print('%s %s', (first_name, last_name))

add_last_name('Jon', 'Gross')

