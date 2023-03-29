x=int(input())
q=1
for i in range(1,x+1):
    p=q
    for j in range(1,i+1):
        print(p,end="")
        p=0 if p==1 else 1
    print()
    q=0 if q==1 else 1