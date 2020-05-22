"""
Retrieving attributes value from objects
"""
class Program:
	language = "Python"
	version = 3.8


# getattr(obj_name(or class name), attribute_name, optional: default)
print(getattr(Program,"version"))
print(getattr(Program,"x", None))

#.dot notation

print(Program.language)

#cant set default in dot notation and unknown attributes will result in attributte error
# print(Program.x)

# Set attributes

# setattr(obj_symbol, attribute_name, attribute_value)

setattr(Program,"version",3.9)
print(getattr(Program,"version"))

# equivalent dot notation
Program.language = "C"
print(Program.language)

"""
setting new attributes is possible in python and will not give any error as python
is dynamically typed language.
"""
setattr(Program,"x",100)
print(getattr(Program,"x"))

"""
Python stores all the class state in dictionary
"""
print(Program.__dict__)

# Delete attributes
# delattr(obj_symbol, attribute_name)
delattr(Program,"x")

print(Program.__dict__)

print(type(Program.__dict__))