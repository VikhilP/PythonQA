firstString = str(input("first word "))
secondString = str(input("second word "))
near = False
print (list(secondString))


j = 0

if secondString > firstString:
    for i in list(secondString):
        l1 = list(firstString)
        l2 = list(secondString)
        

        del(l2[j])
        j = j+1


        edit = "".join(l2)
        print (edit)
        if edit == firstString:
            near = True
            break

if secondString < firstString:
    for i in list(firstString):
        l1 = list(firstString)
        l2 = list(secondString)
        
    
        del(l1[j])
        j = j+1


        edit = "".join(l1)
        print (edit)
        if edit == secondString:
            near = True
            break

    

print(near)