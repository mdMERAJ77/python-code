"""x=int(input())
y=x
ans=0

while x!=0:
    r=x%10
    x=x//10
    ans=ans*10+r
print(ans)
if(ans==y):
    print("is pali")
else:
    print("is not pali")
    
# list alising
li=[1,2,3]
n_li=li
li[1]=7
print(li)
print(n_li)
print(id(li))
print(id(n_li))

#list coning
li=[1,2,3]
n_li=[]
n_li+=li
li[1]=7
print(li)
print(n_li)
print(id(li))
print(id(n_li))

#built in functions on list

len()
max()
min()
sum()
any()
all()
del()
sorted()
reversed()

if all((12>3,20>25,17>15)):
    print("All true")
else:
    print("sum conditon or all conditons or false")
    
if any((12>3,20>25,10>15)):
        print("All true")
else:
    print("sum conditon or all conditons or false")
    
li=['a','b',7,3]
if all(li):
    print("all true")
else:
    print("not all true")

li=['a','b',0,3]
if all(li):
    print("all true")
else:
    print("not all true")
    
#none '' [] () {} 0 0.0 all are false

li=['a','b',0,3]
if all(li):
    print("all true")
else:
    print("not all true")
    
# write a program to check whether a list is empty or not 

li=[]
if (li):
    print("empty")
else:
    print("not empty")
    
li=[1,2,3]
print(li)
del(li)
print(li)
"""





