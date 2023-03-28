x=int(input())
y=x
ans=0
while x!=0:
    r=x%10
    x=x//10
    ans=ans*10+r
print(ans)
if(ans==y):
    print("is palidrome")
else:
    print("is not palidrome")
    
    
    """
    
x=int(input())  
for i in range(x):
    print("*"*x)
    """
    