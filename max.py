lst=eval(input("Enter the list"))#6,8,11,6,12,19,16
ln=len(lst)
mx=max(lst)
ind=lst.index(mx)
if ind<=(ln/2):
    print("The maximum element ",mx,"lies in the 1st half")
else:
    print("The maximum element ",mx,"lies in the 2nd half")


#2 lists and find the max element from elements of both the list combined
lst1=eval(input("Enter the list"))#6,8,11,6,12,19,16
mx1=max(lst1)
lst2=eval(input("Enter the list"))#6,8,11,6,12,19,16
mx2=max(lst2)
if mx1>=mx2:
    print(mx1,"The maximum values is in list1 at index",lst1.index(mx1))
else:
    print(mx2,"The maximum values is in the list2 at index",lst2.index(mx2))


