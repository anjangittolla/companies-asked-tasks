seq=[10,-9,8,15,18,-16]
a=[]
while len(seq)>1:
    first=seq[0]
    for i in seq:
        a.append((first,i,first+i))
    seq.remove(seq[0])
print(a)