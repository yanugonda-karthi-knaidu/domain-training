b=int(input("enter no of blocks: "))
l=int(input("enter no of lines: "))
s=int(input("enter no of stars: "))
for i in range(b):
    c=0
    for j in range(l-i):
        for k in range(s):
            print("*",end=" ")
            c=c+1
        print()
    print(c)
    print("____________")
