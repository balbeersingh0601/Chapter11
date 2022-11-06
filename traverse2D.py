r=int(input("ENter the no. of rows"))
c=int(input("ENter the no. of columnes"))
Lst=[]
for i in range(r):
    row=[]
    for j in range(c):
        elem = int(input("Element "+str(i)+" "+str(j)+":"))
        row.append(elem)
    Lst.append(row)
print("List created is :",Lst)
