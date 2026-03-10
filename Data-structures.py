#Tuple: these are fixed-length and immutable.
#Once assigned, they can not be changed.
#they are comma-separated and wrapped in parenthesis

tup = (1,2,3,4,5)
print(tup)

#parenthese can also be omitted
a = 2,5,6,7
tuple2 = tuple('string')
print(tuple2)
#elements can be accessed through indexing 
print(tuple2[3])
print(tuple2[2])

#unpacking tuples(iterating over tuples ot lists)
seq =[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c, in seq:
    print(f'a={a}, b={b}, c={c}')


#list: they are variable length and immutable meaning they can be modified
#they are define using square barckets[] or list type function 

my_list = [1,2,3,4,5,6]
tup = ('goat', 'cat', 'dog')
mynew_list = list(tup)
print(mynew_list)
mynew_list[2] = 'Dove'
print(mynew_list)
#adding and removing elements 
mynew_list.append('bird') #adding element bird at the end of the list.
print(mynew_list)
#Elements can be inserted at the a specified location
mynew_list.insert(1, 'flower') #the insertion must be between 0 and the length of the list.
print(mynew_list)
#.extend method can be used to append multiple elements to a list
x = ['bird', 1, 5]
x.extend(['hello',1,2,3,])
print(x)
mynew_list.sort()
print(mynew_list)
#secondary sorting by sort key e.g
mynew_list.sort(key=len)
print(mynew_list)

