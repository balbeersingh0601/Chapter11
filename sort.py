val=eval(input("Enter a list"))
print("Original list ",val)
val1=val*2
print("Replacement list ", val)
val2=val.sort()
print("Sorted in ascending order ",val2)
val.sort(reverse=True)
print("Sorted in descending order ",val)