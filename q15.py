#compare 2 list, print first index where they differ
l1=[1,2,3]
l2=[1,2,4]
l=len(l1)
l4=[]
for i in range(l):
    if l1[i]==l2[i]:
        l3=l1[i]
        l4+=[l3]
    else:
        print("The first index where they differ ",i)
        break
print("List containing the same values",l4)