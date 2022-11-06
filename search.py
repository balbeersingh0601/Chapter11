lst=[2,8,9,11,-55,-11,22,27,78,67]
l=len(lst)
ele= int(input("Enter element to be searched :"))
for i in range(l):
    if ele== lst[i]:
        print(ele,"found at index ",i)
        break
else:
    print(ele,"not found")
