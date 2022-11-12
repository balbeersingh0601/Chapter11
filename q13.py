#num=eval(input(" Enter the numerators "))
num=[23,43,61,72,83,94,105,116,128,139,140]
max1=max(num)
print("Max of the list",max1)
min1=min(num)
print("Min of the list",min1)
print("Now!!, Finding max and min for specified range ")
n= int(input("ENter the range(0-n) ?"))
lst=[]
for i in range(n+1):
    mx=num[i]
    lst+=[mx]
print(lst)
max2=max(lst)
print("Max in updated list ",max2)
min2=min(lst)
print("Min in updated liist",min2)
