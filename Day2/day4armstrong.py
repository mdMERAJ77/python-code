x=int(input())
y=t=x
count=0
while x!=0:
    x=x//10
    count=count+1
#print(count)
ans=0
while y!=0:
    rem=y%10    
    ans=ans+(rem**count)
    y=y//10
if (ans==t):
    print("is armstrong")
else:
    print("is not armstrong")