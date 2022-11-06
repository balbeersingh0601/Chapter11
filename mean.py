lst=eval(input("Enter list :"))
l=len(lst)
mean=sum=0
for i in range(l):
    sum+=lst[i]
mean=sum/l
print("Given list ",lst)
print("The mean of the given list ",mean)

