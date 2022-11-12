#print fibonacci
l=[0,1]
n= int(input("Enter the value of n"))
for i in range(1,n):
    l2=l[i]+l[i-1]
    l+=[l2]
print(l)
