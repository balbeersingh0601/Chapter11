#Traversing
L = ['p','y','t','h','o','n']
l=len(L)
for a in range(l):
    print(L[a],end=' ')

#slicing
print()
lst=[10,20,30,40,50,60,70,80,32,34,36,38,65]
print(lst[3:30])
print()
print(lst[-15:7])
print(lst[0:10:2])
print()

#comparing
l1= [1,2,3]
l1 += '4'
print(l1)
l2=[4,5,6]
l3= [1,[2,3],4]
print(l1==l2)
print(l1==l3)


#Modifying
L=['one','two','three']
L[0:2]=[0,1]
print(L)

#copying
L1=[17,24,15,30,34,17]
L2=L1.copy()
print("original List",L1)
print("Created copy of list",L2)
L2[0]+=10
L2[-1]+=10
print("Updated list",L2)
