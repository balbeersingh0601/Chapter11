lst=eval(input("Enter list of numbers between 1 to 12 :"))
print("Original List ",lst)
l=len(lst)
print("Replacing the numbers greater than 10")
for i in range(l):
    if lst[i]<10:
        print(lst[i], end=' ')



