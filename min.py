lst=eval(input("Enter the list :"))
l=len(lst)
min_ele=lst[0]
min_index=0
for i in range(1,l):
    if lst[i]<min_ele:
        min_ele=lst[i]
        min_index=i
print("Given list is ",lst)
print("The min element of given list is :")
print(min_ele,"at index ",min_index)