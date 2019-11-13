#This was asked by ECI Telecom 
#Write a program to find the missing letter in a given Sequence.
def missing(seq):
    length=len(seq)
    total=(length+1)*(length+2)/2
    add=sum(seq)
    return abs(total-add)
seq=[1,2,3,5,6,7]
print(missing(seq))
