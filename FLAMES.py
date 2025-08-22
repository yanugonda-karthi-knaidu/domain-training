a=str(input("Enter your boy name: "))
b=str(input("Enter your girl name: "))
a1=list(a)
b1=list(b)
for i in range(len(a1)):
    for j in range(len(b1)):
        if(a1[i]==b1[j]):
            a1[i]="2"
            b1[j]="2"
print(a1)
print(b1)

c=0
for i  in a1:
    if(i!="2"):
        c=c+1
for i  in b1:
    if(i!="2"):
        c=c+1
print(c)

f=0
res=list("FLAMES")
while(len(res)!=1):
    f=(f+c-1)%len(res)
    res.pop(f)
print("Relationship is: ",res[0])
