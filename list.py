#creating a list
list=[]
print(list)

#list consisting of iteams
list1=[28,27,18,10,2,1]
print(list1)

#list consisting of the string and numeric values and using inserting
list=[1,'apple',28.27]
print(list)
list.insert(1, 'rakesh')
print(list)

#nested list

list=[['apple',28],['banana',27]]
print(list)
list.insert(1,2021)
print(list)



#removing iteams from the list using remove method
list2=[1,'apple',28.27]
list2.remove(1)
print(list2)
list2.remove('apple')
print(list)
list2.remove(28.27)
print(list)

#POP method
list=[1,'cse',2,'ece',3,'eee']
print(list)
list.pop(0)
print(list)
list.pop(2)
print(list)

#APPEND method
list=[1,2,3]
print(list)
list.append('python')
print(list)
list.append(28.27)
print(list)



#length of the list
list=[1,'cse',2,'ece',3,'eee']
print(len(list))
a=len(list)
print(a)

#clear method
list=['cse','ece','eee']
list.clear()
print(list)
z=list.clear()
print(z)




