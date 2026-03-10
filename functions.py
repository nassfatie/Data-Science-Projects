#Functions: there are primary and most important method of code organization and reuse in python
# its defined with a def keyword which is a block of code with an optional use of return keyword

def my_function(x,y):
    return x + y
my_function(1,3)
result = my_function(1,3)
print(result)

def multiplication(a, b):
    return a * b
print(multiplication(2,5))

#functions are objects
import re #used in patterns to match, serach and manupulate text.

states = ["  alabama", "Georgia!", "Georgia", "Fl0rida", "south  carolina##", "West virginia?"]
def clean_strings(strings):
    result=[]
    for value in strings:
        value = value.strip()
        value = re.sub("[!#?]", "", value)
        value = value.title()
        result.append(value)
    return result
print(clean_strings(states))

#itertools function
import itertools
def first_letter(x):
    return x[0]
names = ['Fania', 'Shania', 'Abdul', 'Mary','Jane', 'Benard']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names))