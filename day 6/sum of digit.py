x=int(input())
ans=0
y=x
while x!=0:
    y=x%10
    x=x//10
    ans=ans+y
print(ans)