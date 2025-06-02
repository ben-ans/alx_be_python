size = int(input("Enter the size of the ppattern: "))
i = 1
while i <= size:
    for j in range(1,size+1):
        print("*", end=" ")
    i+=1
    print("\n")