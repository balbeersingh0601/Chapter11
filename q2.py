l=['a','e','i','o','u']
length=len(l)
print("Lenth of list is ",length)
print("Reversal of list is ")
for i in range(-1,-length-1,-1):
    print(l[i],end=" ")
print()
#ANother process
l2=['q','w','e','r','t']
l1=l2.reverse()
print("Reversal in place using reverse method",l2)
print("Here l1 stores a none value as the reversal process is in place ",l1)
