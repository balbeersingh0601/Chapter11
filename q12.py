num=eval(input(" Enter the numerators "))
denum= eval(input("Enter the denominators"))
l=len(num)
lst=[]
print("numerators list ",num)
print("Denominators list ",denum)
print("the list of fractions")
for i in range(l):
    n=num[i]/denum[i]
    lst+=[n]
print(lst)
l1=lst.sort()
print("After sorting the list",lst)
print("the smallest fractions",lst[0])
