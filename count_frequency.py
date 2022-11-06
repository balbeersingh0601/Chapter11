lst=[2,2,2,2,1,2,1,1,1,5,2,5,5,5,6]
l=len(lst)
ele= int(input("Enter element "))
count=0
for i in range(0,l):
    if ele==lst[i]:
        count+=1
if count == 0:
    print(ele,"not found in given list")
else:
    print(ele,"has frequency as ",count,"in the given list ")

#finding frequencies of all the element of a list
l=len(lst)
uniq=[]
dupl=[]
count=i=0
while i<l:
    ele1=lst[i]
    count=1
    if ele1 not in uniq and ele1 not in dupl:
        i+=1
        for j in range(i,l):
            if ele1==lst[j]:
                count+=1
        else:
            print("element ",ele1,"Frequecy ",count)
            if count==1:
                uniq.append(ele1)
            else:
                dupl.append(ele1)
    else:
        i+=1
print("Original list",lst)
print("Unique elements list ",uniq)
print("Duplicate elements list",dupl)


