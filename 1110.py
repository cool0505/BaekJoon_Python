a=input()
if(len(a)==1):
    a='0'+a
c=a
i=1
while(1):
    b=str(int(c[0])+int(c[1]))
    if(len(b)==1):
        c=c[1]+b[0]
    else:
        c=c[1]+b[1]
    if(a==c):
        print(i)
        break
    i=i+1