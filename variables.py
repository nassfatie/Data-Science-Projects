#variables and argument assigning
a = [1,2,4]
b = a 
print(b)

a.append(4)
print(b)

def append_element(some_list, element):
    some_list.append(element)
data = [1,2,4,5]
append_element(data, 6)
print(data)

s = 0.5
x = str(s)
print(x)
print(type(x))