# day of 1
'''
Before continuing we need to understand data types and variables and how to access 'em

For the selenium driver and python, we are gonna use the html references
'''
x = 20 # int
x = 20.5 # float
x = "Jon" # string
x = True # bool
x = {"name" : "Jon", "age" : None}	# dict
print(x['name'])

# access to a dict with dot notation could be a little tricky
class convert_to_dot_notation(dict):
    """
    Access dictionary attributes via dot notation
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


dot_notation = convert_to_dot_notation({"name": "David"})
print(dot_notation.name)