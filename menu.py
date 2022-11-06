val=[17,23,18,19]
print("The list is :",val)
while True:
    print("Main Menu")
    print("1. Insert")
    print("2. Delete")
    print("3. Exit ")
    ch=int(input("Enter you choice 1/2/3"))
    if ch==1:
        item = int(input("Enter item"))
        pos = int(input("Insert at which position ? "))
        index=pos-1
        val.insert(index,item)
        print("Success ! List now is ",val)
    elif ch==2:
        print("Deletion Menu")
        print("1. Delete using Value ")
        print("2. Delete using index ")
        print("3. Delete a sblist ")
        dch = int(input("Enter you choice 1/2/3"))
        if dch ==1:
            item = int(input("ENter item to be deleted : "))
            val.remove(item)
            print("List now is ", val)
        elif dch ==2:
            index = int(input("ENter index of item to deleted :"))
            val.pop(index)
            print("List now is ", val)
        elif dch ==3:
            l=int(input("Enter lower limit of list slice to be deleted "))
            h = int(input("Enter upper limit of list slice to be deleted "))
            del val[l:h]
            print("List now is ",val)
        else:
            print("valid choices are 1/2/3 only")
    elif ch==3:
        break;
    else:
        print("Valid choices are 1/2/3 only ")