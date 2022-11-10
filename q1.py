l=[1,2,3,4,5,6,7,8]
length=len(l)
print("Original list ", l)
print("Value increment with 1")
for i in range(length):
    l[i]+=1
    print(l[i],end=' ')
print()
print("Every value in list is comming twice ",l*2)

l2=[1,2,3]
l2_len=len(l2)
print("Value multiplied with 2")
for i in range(l2_len):
    l2[i]*=2
    print(l2[i],end=' ')