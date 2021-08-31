def add(a,b):
    return a+b
def subt(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
    return g/h
print('1.addition')
print('2.subtraction')
print('3.multiplication')
print('4.division')
choice=int(input('enter your choice'))
if choice==1:
    a=int(input('enter a value'))
    b=int(input('enter b value'))
    print('sum is:',add(a,b))
elif choice==2:
    c=int(input('enter c value'))
    d=int(input('enter d value'))
    print('subtraction is:',subt(c,d))   
elif choice==3:
    e=int(input('enter e value'))
    f=int(input('enter f value'))
    print('multiplication is:',mul(e,f))
elif choice==4:
    g=int(input('enter g value'))
    h=int(input('enter h value'))
    print('division is:',div(g,h))    
else:
    print('invalid choice go to menu')    