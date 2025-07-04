d1={'a':1,'b':2,'c':3}
d2={'a':4,'c':5}
merge={}
for i in d1:
    merge[i]=d1[i]
for i in d2:
    if i in merge:
        merge[i]+=d2[i]
    else:
        merge[i]=d2[i]
print(merge)