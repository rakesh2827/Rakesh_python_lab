def check(list1,list2):
    if len(list1)!=len(list2):
        return False
    return sorted(list1)==sorted(list2)
list11=[16,15,28,27]
list22=[28,27]
if check(list11,list22):
    print('lists are equal')
else:
    print('lists are not equal')    