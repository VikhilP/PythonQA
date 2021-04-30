table = int(input("number"))

for row in range(1,table+1):
    for col in range(1,table+1):
        print (row * col, end=" ")
    print("\n")
