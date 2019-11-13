from itertools import permutations
a="abcd"
b=permutations(a)
c=[]
for i in b:
    c.append(i)
print("******PERMUTATIONS********",c)
print("************************************************")
from itertools import combinations
a="ABCD"
b=combinations(a,2)
print("**************     COMBINATIONS          ****************")
for i in b:
    print(i)
