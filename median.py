lst=eval(input("Enter list :"))
l1=sorted(lst) #using sorted function
l=len(l1)
mid=l//2
if l%2==0:
     m1,m2=mid-1,mid
     med= (lst[m1]+lst[m2])/2
else:
    med = lst[mid]
print("Median of given list",med)
