lst=eval(input("Enter the list"))
print("original list is ",lst)
s=len(lst)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    print(i,i+1)
    lst[i],lst[i+1]=lst[i+1],lst[i]
print("list after swapping ",lst)
