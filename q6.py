#lst=eval(input("Enter list of numbers"))
lst1=[1,2,3,4,5,6,7,8,9,10,11,12,14,15,20]
print("Orginial list",lst1)
l=len(lst1)
count=0
item= int(input("Enter the no. to search ?"))
for i in range(l):
    if lst1[i]==item:
        count+=1
        break

if count>=1:
    print(item, " is present at index", i)
else:
    print("Entered no. is NOT FOUND")



