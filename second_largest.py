'''lst=eval(input("Enter list :"))
l=len(lst)
biggest=secondbiggest = lst[0]
for i in range(1,l):
    if lst[i]>biggest:
        secondbiggest=biggest
        biggest=lst[i]
    elif lst[i]>secondbiggest:
        secondbiggest=lst[i]
print("Largest no. of the list",biggest)
print("Second largest no of the list",secondbiggest)'''

lst=eval(input("Enter list :")) #3,-4,-2,6,7,0,-7,-2,5
plist =[]
nlist=[]
s=len(lst)
for i in range(s):
    if lst[i]<0:
        nlist.append(lst[i])
    elif lst[i]>0:
        plist.append(lst[i])
print("Main list : ",lst)
print("Positive no. list ",plist)
print("Negative no. list ",nlist)