list_of_strings=['My','vikas_chauhan','name','is','deepika']
l=len(list_of_strings)
largest=2
print("Length of list is",l)
for i in range(l):
    str=list_of_strings[i]
    print(str)
    l1=len(str)
    print(l1)
    if l1>largest:
        largest=l1
print("largest string has length ",largest)

list_of_num=[1,1,1,2,3,4,5,6,7]
l2=len(list_of_num)
new_list=[]
for j in range(l2):
    new_list+=list_of_num
print(new_list)

