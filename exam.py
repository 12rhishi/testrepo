num=14335
list=[]
while num:
    a=num/10
    list.append(a)
    num = num//10
c=0
s=1
for x in range(0,len(list)):
    for y in range(s,len(list)):
        if x == list[y]:
            c=c+1
        s=s+1
if c==0:
    print("unique")
else:
    print("not unique")