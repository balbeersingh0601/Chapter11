#lst=eval(input("Enter list :"))
lst = [6,7,1,6,7,2,7,5,75]
item=int(input("Enter element to be removed "))
c=lst.count(item)
if c==0:
    print(item,"not in the list")
else:
    while c>0:
        i=lst.index(item)
        lst.pop(i)
        c=c-1
    print("List after removing ",item," is ::",lst)


#shift all the zeros to right and all the non-zeros to left of the list
'''l=len(lst)
end=l-1
print("Original list ",lst)
i=0
while(i<=end):
    ele=lst[i]
    if ele==0:
        for j in range(i,end):
            lst[j]=lst[j+1]
        else:
            lst[end]=0
    if lst[i]!=0:
        i+=1

print("zero shifted : ",lst)'''
