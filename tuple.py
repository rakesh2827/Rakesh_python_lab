#creating a tuple
tuple=()
print(tuple)
#tuple with values
tuple=(1,'python',2.2,'pp')
print(tuple)
print(tuple[1])
#nested tuples
tuple=((1,2),('python'))
print(tuple)

#tuple methods
tuple=((1,2,3,4,'a','b','c'),('cse','it'))
#length of the tuple
print(len(tuple))
#accessing tuple elements 
print(tuple[0][3])
print(tuple[0][6])
print(tuple[1][0])
#negative indexing
print(tuple[0][-6])
#checking for element in the tuple
print(1 in tuple[0])
print('cse' in tuple[1])
if 'cse' in tuple[1]:
    print('key present')
else:
    print('not found')    

