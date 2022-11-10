lst=eval(input("Enter list of string"))
print("Original List ",lst)
l=len(lst)
print("Slicing the list ",lst[1:l])
print("New list with one character removed")
for i in range(l):
    l2=lst[i]
    print(l2[1:],end=" , ")